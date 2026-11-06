from fastapi import APIRouter
from ledger.accounts import accounts
from fastapi import HTTPException
from pydantic import BaseModel
from ledger.transactions import create_transaction, get_transactions


class Account(BaseModel):
    name: str
    currency: str

router = APIRouter()

@router.get("/")
def read_root():
    return {
        "name": "Ledger",
        "description": "Financial Ledger System",
        "status": "operational",
        "version": "0.1.0"
    }

@router.get("/accounts")
def get_acc():
    return {"accounts": accounts}

@router.post("/addacc")
def add_acc(data: Account):
    new_acc = {
"id": len(accounts)+1,
"name": data.name,
"currency": data.currency,
"balance": 0
}
    accounts.append(new_acc)
    return new_acc

@router.get("/accounts/{account_id}")
def by_accid(account_id: int):
    result = next((x for x in accounts if x["id"] == account_id ),None)
    if result is None:
        raise HTTPException(
    status_code=404,
    detail="Account not found"
)
    else:
        return result

class WithdrawRequest(BaseModel):
    amount: float
@router.post("/accounts/{account_id}/withdraw")
def withdraw(account_id: int,data: WithdrawRequest):
    result = next((x for x in accounts if x["id"] == account_id), None)
    if result is None:
        raise HTTPException(
    status_code=404,
    detail="Account not found"
)
    if data.amount <=0:
        raise HTTPException(
            status_code=400,
            detail="Invalid withdrawal amount"
        )
    if data.amount > result["balance"]:
        raise HTTPException(
            status_code=400,
            detail="Withdraw amount cannot br greater than balance"
)
    else:
        result["balance"] -= data.amount
        create_transaction(
            amount=data.amount,
            from_account=account_id,
            to_account=None,
            transaction_type="withdrawal"
        )
        return result

class DepositRequest(BaseModel):
    amount: float
@router.post("/accounts/{account_id}/deposit")
def deposit(account_id: int,data: DepositRequest):
    result = next((x for x in accounts if x["id"] == account_id), None)
    if result is None:
        raise HTTPException(
    status_code=404,
    detail="Account not found"
)
    if data.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid deposit amount"
)
    else:
        result["balance"] += data.amount
        create_transaction(
    amount=data.amount,
    from_account=None,
    to_account=account_id,
    transaction_type="deposit"
)
        return result

class TransferRequest(BaseModel):
    from_account: int
    to_account: int
    amount: float
@router.post("/transfer")
def transfer(data: TransferRequest):
    result1 = next((x for x in accounts if x["id"]==data.from_account),None)
    result2 = next((x for x in accounts if x["id"]==data.to_account),None)
    if result1 is None or result2 is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    if data.amount <=0:
        raise HTTPException(
            status_code=400,
            detail="Invalid amount"
        )
    if result1["id"]==result2["id"]:
        raise HTTPException(
            status_code=400,
            detail="Source and receiver cannot be the same"
        )
    if result1["balance"]<data.amount:
        raise HTTPException(
            status_code=400,
            detail="Insufficient balance"
        )
    if result1["currency"] != result2["currency"]:
        raise HTTPException(
            status_code=400,
            detail="cannnot tramsfer between two different currency"
        )
    result1["balance"] -= data.amount
    result2["balance"] += data.amount
    create_transaction(
            amount=data.amount,
            from_account=data.from_account,
            to_account=data.to_account,
            transaction_type="transfer"
        )
    return {
        "from_account": result1,
        "to_account": result2
    }

@router.get("/transactions")
def read_transactions():
    return get_transactions()

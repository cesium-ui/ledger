from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "name": "Ledger",
        "description": "Financial Ledger System",
        "status": "operational",
        "version": "0.1.0"
    }

accounts = [
    {"id": 1,
    "name": "Alice",
    "currency": "INR",
    "balance": 10000},
    {"id": 2,
    "name": "Bob",
    "currency": "INR",
    "balance": 5000
    }
]
@app.get("/accounts")
def get_acc():
    return {"accounts": accounts}


class Account(BaseModel):
    name: str
    currency: str

@app.post("/addacc")
def add_acc(data: Account):
    new_acc = {
"id": len(accounts)+1,
"name": data.name,
"currency": data.currency,
"balance": 0
}
    accounts.append(new_acc)
    return new_acc

@app.get("/accounts/{account_id}")
def by_accif(account_id: int):
    result = next((x for x in accounts if x["id"] == account_id ),None)
    if result is None:
        raise HTTPException(
    status_code=404,
    detail="Account not found"
)
    else:
        return result

class DepositRequest(BaseModel):
    amount: float
@app.post("/accounts/{account_id}/deposit")
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
        return result["balance"]




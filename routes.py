
from decimal import Decimal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ledger.accounts import (
    create_account,
    get_account,
    get_all_accounts,
    deposit as deposit_account,
    withdraw as withdraw_account,
    transfer_account,
)
from ledger.transactions import get_transactions


router = APIRouter()


# Request Models

class CreateAccountRequest(BaseModel):
    name: str
    currency: str


class DepositRequest(BaseModel):
    amount: Decimal


class WithdrawRequest(BaseModel):
    amount: Decimal


class TransferRequest(BaseModel):
    from_account: int
    to_account: int
    amount: Decimal


# Root

@router.get("/")
def read_root():
    return {
        "name": "Ledger",
        "description": "Financial Ledger System",
        "status": "operational",
        "version": "0.1.0"
    }


# Accounts

@router.get("/accounts")
def get_acc():
    return {"accounts": get_all_accounts()}


@router.post("/addacc")
def add_acc(data: CreateAccountRequest):
    return create_account(
        name=data.name,
        currency=data.currency
    )


@router.get("/accounts/{account_id}")
def by_accid(account_id: int):
    result = get_account(account_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return result


# Withdrawals

@router.post("/accounts/{account_id}/withdraw")
def withdraw(account_id: int, data: WithdrawRequest):

    if data.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid withdrawal amount"
        )

    account = get_account(account_id)

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    if data.amount > account.balance:
        raise HTTPException(
            status_code=400,
            detail="Insufficient balance"
        )

    result = withdraw_account(account_id, data.amount)

    # Record the transaction
    from ledger.transactions import create_transaction

    create_transaction(
        amount=data.amount,
        from_account=account_id,
        to_account=None,
        transaction_type="withdrawal"
    )

    return result


# Deposits

@router.post("/accounts/{account_id}/deposit")
def deposit(account_id: int, data: DepositRequest):

    if data.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid deposit amount"
        )

    result = deposit_account(account_id, data.amount)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    # Record the transaction
    from ledger.transactions import create_transaction

    create_transaction(
        amount=data.amount,
        from_account=None,
        to_account=account_id,
        transaction_type="deposit"
    )

    return result


# Transfers

@router.post("/transfer")
def transfer(data: TransferRequest):

    try:
        result = transfer_account(
            data.from_account,
            data.to_account,
            data.amount
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return result


# Transactions

@router.get("/transactions")
def read_transactions():
    return get_transactions()

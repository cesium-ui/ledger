transactions = []
def get_transactions():
    return transactions

def create_transaction(amount: float,
    from_account: int,
    to_account: int,
    transaction_type: str):
    transaction_id = len(transactions)+1
    transaction = {
        "id": transaction_id,
        "type": transaction_type,
        "amount": amount,
        "from_account": from_account,
        "to_account": to_account
    }
    transactions.append(transaction)
    return transaction


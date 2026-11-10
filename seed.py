from database import SessionLocal
from models import Account
from decimal import Decimal

db = SessionLocal()
alice = Account(
    name = "Alice",
    currency = "INR",
    balance =  Decimal(10000.00))
try:
    db.add(alice)
    db.commit()
finally:
    db.close()

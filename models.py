from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from decimal import Decimal

class Account(Base):
    __tablename__ = "accounts"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String,nullable=False)
    currency : Mapped[str] = mapped_column(String,nullable=False)
    balance : Mapped[Decimal] = mapped_column(Numeric(15,2),nullable=False)

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    from_account: Mapped[int | None] = mapped_column(Integer, nullable=True)
    to_account: Mapped[int | None] = mapped_column(Integer, nullable=True)
from sqlalchemy import Column, Integer, ForeignKey, String, Float, DateTime
from src.main.api.db.base import Base

class Transfer(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True)
    to_account_id = Column(Integer, ForeignKey('transaction.id'), nullable=False)
    from_account_id= Column(Integer, unique=True, nullable=False)
    credit_id = Column(Integer, unique=True, nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Transaction({self.to_account_id}, {self.from_account_id}, {self.amount}, {self.transaction_type}, {self.created_at})>"

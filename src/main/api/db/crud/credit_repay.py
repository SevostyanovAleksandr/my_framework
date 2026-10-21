from sqlalchemy.orm import Session
from src.main.api.db.models.transfer_table import Transfer

class CredidRepayCrudDB:
    @staticmethod
    def get_credit_repay_by_from_to_amount(db: Session, amount: float, credit_id: int) -> Transfer | None:
        return db.query(Transfer).filter(Transfer.amount == amount, Transfer.credit_id == credit_id).first()

    @staticmethod
    def count_all(db_session: Session) -> int:
        return db_session.query(Transfer).count()
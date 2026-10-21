from sqlalchemy.orm import Session
from src.main.api.db.models.transfer_table import Transfer

class TransferCrudDB:
    @staticmethod
    def get_transfer_by_from_to_amount(db: Session, from_account_id: int, to_account_id: int, amount: float) -> Transfer | None:
        return db.query(Transfer).filter( Transfer.from_account_id == from_account_id, Transfer.to_account_id == to_account_id, Transfer.amount == amount).first()

    @staticmethod
    def count_all(db_session: Session) -> int:
        return db_session.query(Transfer).count()
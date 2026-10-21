from sqlalchemy.orm import Session
from src.main.api.db.models.account_table import Account

class DepositCrudDB:
    @staticmethod
    def get_deposit_by_id(db: Session, account_id: int) -> Account | None:
        return db.query(Account).filter_by(id = account_id).first()

    @staticmethod
    def count_all(db_session: Session) -> int:
        return db_session.query(Account).count()
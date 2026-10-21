from sqlalchemy.orm import Session
from src.main.api.db.models.credit_table import Credit

class CredidCrudDB:
    @staticmethod
    def get_credit_by_from_to_amount(db: Session, amount: float, term_months: int) -> Credit | None:
        return db.query(Credit).filter(Credit.amount == amount, Credit.term_months == term_months).first()

    @staticmethod
    def count_all(db_session: Session) -> int:
        return db_session.query(Credit).count()
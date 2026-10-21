from sqlalchemy.orm import Session
from src.main.api.db.models.user_table import User

class UserCrudDB:
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> User | None :
        return db.query(User).filter_by(User.username == username).first()


from sqlalchemy.orm import Session

from classes.api_manager import ApiManager
from fixtures.api_fixture import api_manager
from fixtures.db_fixture import db_session
from models.create_user_request import CreateUserRequest
from src.main.api.db.crud.accoutn_crud import AccoutnCrudDB as Account


class TestAppAccount:
    #Позитивный сценарий
    #Авторизация только что созданного пользователя
    def test_create_bank_account_valid(self, api_manager, create_user_request, db_session: Session):
        response = api_manager.user_steps.create_account(create_user_request)

        assert response.balance == 0

        account_from_db = Account.get_account_by_id(db_session, response.id)
        assert account_from_db.id == response.id , "Аккаунт не создан, id нет в базе данных"
        assert account_from_db.balance == response.balance


    def test_create_bank_account_invalid403(self, api_manager, db_session: Session):
        # Попытка создания счета под админом
        before_account = Account.count_all(db_session)
        api_manager.user_steps.create_account_invalid_403()
        after_account = Account.count_all(db_session)

        assert before_account == after_account , "Аккаунт создан ошибка"





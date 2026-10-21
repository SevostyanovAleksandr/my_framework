import pytest
from sqlalchemy.orm import Session

from src.main.api.db.crud.deposit_crud import DepositCrudDB as Deposit


@pytest.mark.api
class TestDepositAccount:
    #Пополнение счета
    #Валидный тест на создание счета
    def test_deposit_account_valid(self, api_manager, deposit_account_request, db_session: Session):
        create_user_req, deposit_account_req = deposit_account_request # распаковка
        response = api_manager.user_steps.deposit_account_valid(create_user_req, deposit_account_req)

        assert response.balance == deposit_account_req.amount

        deposit_from_db = Deposit.get_deposit_by_id(db_session, response.id)
        assert deposit_from_db.id == deposit_account_req.accountId, "Нет акаунта в базе"
        assert deposit_from_db.balance == deposit_account_req.amount


    #Некорректный тест некорреткное тело запроса ОР 400
    def test_deposit_account_valid_400(self, api_manager, deposit_account_request_400, db_session: Session):
        create_user_req,  deposit_account_req = deposit_account_request_400 # распаковка
        #Проверка что небыло изменений в бд
        before_account = Deposit.count_all(db_session)

        api_manager.user_steps.deposit_account_invalid_400(create_user_req, deposit_account_req)

        after_account = Deposit.count_all(db_session)

    #Некорректный тест пользователь не авторизаован ОР 401
    def test_deposit_account_valid_401(self, api_manager, deposit_account_request_401, db_session: Session):
        deposit_account_req = deposit_account_request_401 # распаковка
        #Проверка что небыло изменений в бд
        before_account = Deposit.count_all(db_session)

        api_manager.user_steps.deposit_account_invalid_401(deposit_account_req)

        after_account = Deposit.count_all(db_session)


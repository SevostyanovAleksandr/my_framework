import pytest
from sqlalchemy.orm import Session

from fixtures.db_fixture import db_session
from src.main.api.db.crud.transfer_crud import TransferCrudDB as Transfer


@pytest.mark.api
class TestTransferAccount:
    #Валидный сценарий создания пользователя, создание счета двух у одного пользователя, перевод с одного счета на другой
    def test_transfer_account_valid(self, api_manager, transfer_account_valid, db_session: Session):
        create_user_req, id_account_1, id_account_2, deposit_account_req, transfer_account_req = transfer_account_valid
        response = api_manager.user_steps.transfer_account_valid (create_user_req, transfer_account_req)

        assert response.fromAccountId == transfer_account_req.fromAccountId
        assert response.toAccountId == transfer_account_req.toAccountId

        transfer_from_db = Transfer.get_transfer_by_from_to_amount(
            db_session,
            transfer_account_req.fromAccountId,
            transfer_account_req.toAccountId,
            transfer_account_req.amount
        )
        # Проверяем, что запись найдена
        assert transfer_from_db is not None, "Перевод не найден в БД"
        assert transfer_from_db.from_account_id == transfer_account_req.fromAccountId
        assert transfer_from_db.to_account_id == transfer_account_req.toAccountId


    #Не валидный сценарий, ,без авторизации.
    def test_transfer_account_invalid_401(self, api_manager, transfer_account_invalid_401, db_session: Session):
        deposit_account_req, transfer_account_req, id_account_1, id_account_2 = transfer_account_invalid_401
        #Проверка что небыло изменений в бд
        before_account = Transfer.count_all(db_session)
        api_manager.user_steps.transfer_account_invalid_401 (transfer_account_req)
        after_account = Transfer.count_all(db_session)





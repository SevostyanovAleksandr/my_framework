import pytest
from sqlalchemy.orm import Session
from src.main.api.db.crud.credit_request import CredidCrudDB as Credit
@pytest.mark.api
class TestCreditRequest:
    #Валидный сценарий создание пользователя из под админа, c ролью кредит секрет, создади у пользвателя счет, выполнили запрос на получение кредита
    def test_credit_request_valid(self, api_manager, credit_request_valid, db_session: Session):
        create_user_req, id_account_1, credit_request_req = credit_request_valid
        response = api_manager.user_steps.credit_request_valid(create_user_req, credit_request_req)

        assert response.amount == credit_request_req.amount
        assert response.termMonths == credit_request_req.termMonths

        credit_req_from_db = Credit.get_credit_by_from_to_amount(
            db_session,
            credit_request_req.amount,
            credit_request_req.termMonths
        )

        assert credit_req_from_db.term_months == credit_request_req.termMonths
        assert credit_req_from_db.amount == credit_request_req.amount

    #взятие кредита у одного и того же пользователя
    def test_credit_request_invalid404(self, api_manager, credit_request_invalid_404, db_session: Session ):
        create_user_req, id_account_1, credit_request_req = credit_request_invalid_404
        before_account = Credit.count_all(db_session)

        api_manager.user_steps.credit_request_invalid_404(create_user_req, credit_request_req)
        after_account = Credit.count_all(db_session)






import pytest
from sqlalchemy.orm import Session
from src.main.api.db.crud.credit_repay import CredidRepayCrudDB as CreditR

@pytest.mark.api
class TestCreditRepay:
    #Полностью погашенный кредит
    def test_credit_repay_valid(self, api_manager,credit_repay_valid, db_session: Session):
        create_user_req, creditId_req, credit_repay_req, amount_req, id_account_1 = credit_repay_valid
        response = api_manager.user_steps.credit_repay_valid(create_user_req, credit_repay_req)

        assert response.amountDeposited == credit_repay_req.amount
        assert credit_repay_req.creditId == creditId_req

        credit_repay_from_db = CreditR.get_credit_repay_by_from_to_amount(
            db_session,
            credit_repay_req.amount,
            credit_repay_req.creditId,
        )

        assert credit_repay_from_db.credit_id == credit_repay_req.creditId
        assert credit_repay_from_db.amount == credit_repay_req.amount

    #Запрос на погашение частично
    def test_credit_repay_invalid422(self, api_manager,credit_repay_invalid_422, db_session: Session):
        create_user_req, creditId_req, credit_repay_req, amount_req, id_account_1 = credit_repay_invalid_422
        before_account = CreditR.count_all(db_session)

        response = api_manager.user_steps.credit_repay_invalid(create_user_req, credit_repay_req)

        after_account = CreditR.count_all(db_session)


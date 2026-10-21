import pytest

from models.create_user_request import CreateUserRequest
from models.credit_request_request import CreditRequestRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest

#Создает пользователя до выполнения запроса
@pytest.fixture
def create_user_request(api_manager):
    create_user_req = CreateUserRequest(username="sdLev32",password="Pas!sw0rd",role="ROLE_USER")
    api_manager.admin_steps.create_user(create_user_req)
    return create_user_req

@pytest.fixture
def deposit_account_request(api_manager):
    #Создание пользователя
    create_user_req = CreateUserRequest(username="ArLev1ass",password="Pas!sw0rd",role="ROLE_USER")
    api_manager.admin_steps.create_user(create_user_req)
    # Создаем аккаунт
    create_account_req = api_manager.user_steps.create_account(create_user_req)

    id_account = create_account_req.id

    deposit_account_req = DepositAccountRequest(accountId = id_account,amount = 1000)

    return create_user_req, deposit_account_req

@pytest.fixture
def deposit_account_request_400(api_manager):
    #Создание пользователя
    create_user_req = CreateUserRequest(username="ALev31s",password="Pas!sw0rd",role="ROLE_USER")
    api_manager.admin_steps.create_user(create_user_req)
    # Создаем аккаунт
    create_account_req = api_manager.user_steps.create_account(create_user_req)

    id_account = create_account_req.id

    deposit_account_req = DepositAccountRequest(accountId = id_account,amount = 1000)

    return create_user_req, deposit_account_req

@pytest.fixture
def deposit_account_request_401(api_manager):
    #Создание пользователя
    create_user_req = CreateUserRequest(username="ALev41s",password="Pas!sw0rd",role="ROLE_USER")
    api_manager.admin_steps.create_user(create_user_req)
    # Создаем аккаунт
    create_account_req = api_manager.user_steps.create_account(create_user_req)

    id_account = create_account_req.id

    deposit_account_req = DepositAccountRequest(accountId = id_account,amount = 1000)

    return deposit_account_req


@pytest.fixture
def transfer_account_valid(api_manager):
    create_user_req = CreateUserRequest(username="ALev5asd",password="Pas!sw0rd",role="ROLE_USER")
    api_manager.admin_steps.create_user(create_user_req)
    #Создали счет 2
    create_account_req_1 = api_manager.user_steps.create_account(create_user_req)
    id_account_1 = create_account_req_1.id
    #Создали счет 1
    create_account_req_2 = api_manager.user_steps.create_account(create_user_req)
    id_account_2 = create_account_req_2.id

    #Пополнили счет 1
    deposit_account_req = DepositAccountRequest(accountId = id_account_1, amount = 1000)
    api_manager.user_steps.deposit_account_valid( create_user_req, deposit_account_req)
    #Перевод со счета один в счет два
    transfer_account_req = TransferAccountRequest (fromAccountId = id_account_1, toAccountId = id_account_2, amount = 500)
    return create_user_req, id_account_1, id_account_2, deposit_account_req, transfer_account_req

@pytest.fixture
def transfer_account_invalid_401(api_manager):
    create_user_req = CreateUserRequest(username="ALevr6qss",password="Pas!sw0rd",role="ROLE_USER")
    api_manager.admin_steps.create_user(create_user_req)
    #Создали счет 2
    create_account_req_1 = api_manager.user_steps.create_account(create_user_req)
    id_account_1 = create_account_req_1.id
    #Создали счет 1
    create_account_req_2 = api_manager.user_steps.create_account(create_user_req)
    id_account_2 = create_account_req_2.id

    #Пополнили счет 1
    deposit_account_req = DepositAccountRequest(accountId = id_account_1,amount = 1000)
    #Перевод со счета один в счет два
    transfer_account_req = TransferAccountRequest (fromAccountId = id_account_2, toAccountId = id_account_1, amount = 500)
    # не возврашаем create_user_req
    return  deposit_account_req, transfer_account_req, id_account_1, id_account_2

@pytest.fixture
def credit_request_valid(api_manager):
    create_user_req = CreateUserRequest(username="ALevr7dss",password="Pas!sw0rd",role="ROLE_CREDIT_SECRET")
    api_manager.admin_steps.create_user(create_user_req)
    #Создали счет 1
    create_account_req_1 = api_manager.user_steps.create_account(create_user_req)
    id_account_1 = create_account_req_1.id
    credit_request_req = CreditRequestRequest(accountId = id_account_1, amount = 10000, termMonths = 12 )
    return create_user_req, id_account_1 ,credit_request_req

@pytest.fixture
def credit_request_invalid_404(api_manager):
    create_user_req = CreateUserRequest(username="ALev8sas",password="Pas!sw0rd",role="ROLE_CREDIT_SECRET")
    api_manager.admin_steps.create_user(create_user_req)

    # Создали счет 1
    create_account_req_1 = api_manager.user_steps.create_account(create_user_req)
    #Передали не сущесвтуюший айди
    id_account_1 = 1123
    #
    credit_request_req = CreditRequestRequest(accountId = id_account_1, amount = 10000, termMonths = 12 )
    return create_user_req, id_account_1 ,credit_request_req

@pytest.fixture
def credit_repay_valid(api_manager):
    create_user_req = CreateUserRequest(username="Lev9dssqsw",password="Pas!sw0rd",role="ROLE_CREDIT_SECRET")
    api_manager.admin_steps.create_user(create_user_req)
    #Создали счет 1
    create_account_req_1 = api_manager.user_steps.create_account(create_user_req)
    id_account_1 = create_account_req_1.id
    #Взяли кредит
    credit_request_req = CreditRequestRequest(accountId = id_account_1, amount = 10000, termMonths = 12 )
    credit_req = api_manager.user_steps.credit_request_valid(create_user_req, credit_request_req)
    creditId_req = credit_req.creditId
    amount_req = credit_req.amount

    credit_repay_req = CreditRepayRequest(creditId = creditId_req, accountId = id_account_1, amount = amount_req )
    return create_user_req, creditId_req, credit_repay_req, amount_req, id_account_1

@pytest.fixture
def credit_repay_invalid_422(api_manager):
    create_user_req = CreateUserRequest(username="LevAr10as",password="Pas!sw0rd",role="ROLE_CREDIT_SECRET")
    api_manager.admin_steps.create_user(create_user_req)
    #Создали счет 1
    create_account_req_1 = api_manager.user_steps.create_account(create_user_req)
    id_account_1 = create_account_req_1.id
    #Взяли кредит
    credit_request_req = CreditRequestRequest(accountId = id_account_1, amount = 10000, termMonths = 12 )
    credit_req = api_manager.user_steps.credit_request_valid(create_user_req, credit_request_req)
    creditId_req = credit_req.creditId
    amount_req = credit_req.amount - 1000

    credit_repay_req = CreditRepayRequest(creditId = creditId_req, accountId = id_account_1, amount = amount_req )
    return create_user_req, creditId_req, credit_repay_req, amount_req, id_account_1












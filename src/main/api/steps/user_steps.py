from fondation.endpoint import Endpoint
from fondation.requesters.validate_crud_requester import ValidateCrudRequester
from models import create_user_request
from models.create_user_request import CreateUserRequest
from models.credit_repay_request import CreditRepayRequest
from models.deposit_account_request import DepositAccountRequest
from specs.request_specs import RequestSpec
from specs.responce_specs import ResponseSpec
from steps.base_steps import BaseSteps
from fondation.requesters.crud_requester import CrudRequester
from models.transfer_account_request import TransferAccountRequest
from models.credit_request_request import CreditRequestRequest

class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpec.auth_header(create_user_request.username, create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpec.status_code_201()
        ).post()
        return response

    def create_account_invalid_403(self):
      CrudRequester(
            RequestSpec.auth_header(username = "admin",password="123456"),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpec.status_code_403()
        ).post()

    def deposit_account_valid(self, create_user_request: CreateUserRequest, deposit_account_request: DepositAccountRequest):
        response = ValidateCrudRequester(
            RequestSpec.auth_header(create_user_request.username, create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpec.status_code_200()
        ).post(deposit_account_request)
        return response

    def deposit_account_invalid_400(self, create_user_request: CreateUserRequest, deposit_account_request: DepositAccountRequest):
        CrudRequester(
            RequestSpec.auth_header(create_user_request.username, create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpec.status_code_400()
        ).post(deposit_account_request)

    def deposit_account_invalid_401(self,deposit_account_request: DepositAccountRequest):
        CrudRequester(
            RequestSpec.no_auth_header(),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpec.status_code_401()
        ).post(deposit_account_request)

    def transfer_account_valid(self, create_user_request: CreateUserRequest, transfer_account_request: TransferAccountRequest):
        response = ValidateCrudRequester(
            RequestSpec.auth_header(create_user_request.username, create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpec.status_code_200()
        ).post(transfer_account_request)
        return response

    def transfer_account_invalid_401(self, transfer_account_request: TransferAccountRequest):
        response = CrudRequester(
            RequestSpec.no_auth_header(),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpec.status_code_401()
        ).post(transfer_account_request)

    def credit_request_valid(self, create_user_request: CreateUserRequest, credit_request_request: CreditRequestRequest):
        response = ValidateCrudRequester(
            RequestSpec.auth_header(create_user_request.username, create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpec.status_code_201()
        ).post(credit_request_request)
        return response

    def credit_request_invalid_404(self, create_user_request: CreateUserRequest, credit_request_request: CreditRequestRequest):
        response = CrudRequester(
            RequestSpec.auth_header(create_user_request.username, create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpec.status_code_404()
        ).post(credit_request_request)

    def credit_repay_valid(self, create_user_request: CreateUserRequest, credit_repay_request: CreditRepayRequest):
        response = ValidateCrudRequester(
            RequestSpec.auth_header(create_user_request.username, create_user_request.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpec.status_code_200(),
        ).post(credit_repay_request)
        return response

    def credit_repay_invalid(self, create_user_request: CreateUserRequest, credit_repay_request: CreditRepayRequest):
        response = CrudRequester(
            RequestSpec.auth_header(create_user_request.username, create_user_request.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpec.status_code_422(),
        ).post(credit_repay_request)

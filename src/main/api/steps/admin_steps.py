from fondation.endpoint import Endpoint
from fondation.requesters.crud_requester import CrudRequester
from fondation.requesters.validate_crud_requester import ValidateCrudRequester
from models.auth_login_request import AuthLoginRequest
from models.create_user_request import CreateUserRequest
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.specs.responce_specs import ResponseSpec
from src.main.api.specs.request_specs import RequestSpec



class AdminSteps(BaseSteps):
    def create_user(self, create_user_request : CreateUserRequest):
        response = ValidateCrudRequester(
           RequestSpec.auth_header(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER,
           ResponseSpec.status_code_200()

        ).post(create_user_request)

        self.create_obj.append(response)
        return response

    def create_user_invalid400(self, create_user_request : CreateUserRequest):
            CrudRequester(
            RequestSpec.auth_header(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpec.status_code_400()
        ).post(create_user_request)

    def create_user_invalid401(self, create_user_request : CreateUserRequest):
            CrudRequester(
            RequestSpec.no_auth_header(),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpec.status_code_401()
        ).post(create_user_request)

    def login_user_valid(self, auth_login_request : AuthLoginRequest ):
        response = ValidateCrudRequester(
            RequestSpec.no_auth_header(),
            Endpoint.USER_LOGIN,
            ResponseSpec.status_code_200()
        ).post(auth_login_request)
        return response

    def login_user_invalid400(self, auth_login_request : AuthLoginRequest):
        response = CrudRequester(
            RequestSpec.no_auth_header(),
            Endpoint.USER_LOGIN,
            ResponseSpec.status_code_400()
        ).post(auth_login_request)

    def login_user_invalid401(self, auth_login_request : AuthLoginRequest):
        response = CrudRequester(
            RequestSpec.no_auth_header(),
            Endpoint.USER_LOGIN,
            ResponseSpec.status_code_401()
        ).post(auth_login_request)

    def delete_user(self, user_id: int):
        CrudRequester(
            RequestSpec.auth_header(username="admin", password="123456"),
            Endpoint.ADMIN_DELETE_USER,
            ResponseSpec.status_code_200(),
        ).delete(user_id)


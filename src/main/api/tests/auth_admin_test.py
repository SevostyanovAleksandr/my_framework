import pytest

from classes import api_manager
from models import create_user_request
from src.main.api.models.auth_login_request import AuthLoginRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.requests.create_user_requester import CreateUserRequester
from src.main.api.specs.request_specs import RequestSpec
from src.main.api.specs.responce_specs import ResponseSpec
from src.main.api.requests.auth_login_requester import LoginUserRequester



class TestAuthAdmin:
    #Позитивный сценарий авторизации админ
    def test_auth_admin_valid(self, api_manager):
        auth_admin_request = AuthLoginRequest(username="admin", password="123456")
        response = api_manager.admin_steps.login_user_valid(auth_admin_request)

        #Проверка на статус код
        assert response.user.username == auth_admin_request.username
        assert response.user.role == "ROLE_ADMIN"


    @pytest.mark.parametrize(
        "username,password",
        [
            ("", "123456"), #ОР 400 не передал логин
            ("admin", ""), #ОР 400 не передал пароль
        ]
    )
    #Негативный сценарий авторизации под админом
    def test_auth_admin_invalid400(self, username, password, api_manager):
        auth_admin_request = AuthLoginRequest(username=username, password=password)
        api_manager.admin_steps.login_user_invalid400(auth_admin_request)


    @pytest.mark.parametrize(
            "username,password",
            [
                ("admi", "123456"), #Неверный логин ОР 401
                ("admin", "12345"), #Неверный пороль ОР 401
            ]
        )

        #Негативный сценарий авторизация под админом неверный логин и пороль
    def test_auth_admin_login_invalid401(self, username, password, api_manager):
        auth_admin_request = AuthLoginRequest(username=username, password=password)
        api_manager.admin_steps.login_user_invalid401(auth_admin_request)


        #Второй класс с пррверкой атворизации пользователя
        # Позитивный сценарий авторизации под админом
    def test_auth_create_user_valid(self, api_manager, create_user_request):
    #Позитивный сценарий создания пользователя
        response = api_manager.admin_steps.login_user_valid(create_user_request)

        assert response.user.username == create_user_request.username
        assert response.user.role == create_user_request.role


    def test_auth_create_user_invalid(self, api_manager, create_user_request):
        auth_admin_request = AuthLoginRequest(username="Max000", password="Pas!sw0rd")
        api_manager.admin_steps.login_user_invalid401(auth_admin_request)


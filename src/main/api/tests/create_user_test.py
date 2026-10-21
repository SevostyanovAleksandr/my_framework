import pytest

from classes.api_manager import ApiManager
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.requests.create_user_requester import CreateUserRequester
from src.main.api.specs.request_specs import RequestSpec
from src.main.api.specs.responce_specs import ResponseSpec
from src.main.api.steps.admin_steps import AdminSteps
from sqlalchemy.orm import Session
from src.main.api.db.crud.user_crud import UserCrudDB


class TestCreateUser:
    def test_create_user_valid(self, api_manager: ApiManager, db_session: Session):


        create_user_request = CreateUserRequest(username="Tonya11", password="Pas!sw0rd", role="ROLE_USER")
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        user_from_db = UserCrudDB.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username


    #Проверка негативных сценариев логин пароль ОР 400
    @pytest.mark.parametrize(
        "username,password",
        [ ("Kirill1234561", "Всемп1иве№!"),#Негативный сценарий пороль с киррилицей
          ("Kirill12345671", "R!3567"), #Негатиынй сценарий пароль меньше 8 символов
          ("Kirill123456781", "!sd1sdasdasd" ),#Негативный минимум одна одна заглавная
          ("Kirill123456781", "ASDA1DASDA!D"),#Негативный минимум одна маленькая буква
          ("Kirill123456781", "A1ASDAsD"), # Мининум один спец символ
          ("Kirill12345671", "ASDASDASD!a") #Миниму одна цирфа

        ]
    )
    def test_create_user_invalid(self, username, password, api_manager: ApiManager, db_session: Session):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        api_manager.admin_steps.create_user_invalid400(create_user_request)

        user_from_db = UserCrudDB.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db is None, "Пользователь создан ошибка"

    #Проверка негативного отсутсвие токена авторизации ОР 401
    def test_create_user_invalid_token(self, api_manager: ApiManager, db_session: Session):
        create_user_request = CreateUserRequest(username="Kirill12345678", password="Pas!sw0rd", role="ROLE_USER")
        api_manager.admin_steps.create_user_invalid401(create_user_request)

        user_from_db = UserCrudDB.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db is None, "Пользователь создан ошибка"
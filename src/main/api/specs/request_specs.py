import requests
from configs.config import Config
from src.main.api.models.auth_login_request import AuthLoginRequest
from src.main.api.models.auth_login_response import AuthLoginResponse

class RequestSpec:
    @staticmethod
    def base_header():
        return {
            "Content-Type": "application/json",
            "accept": "application/json",
        }
    @staticmethod
    def auth_header(username: str, password: str):
        request = AuthLoginRequest(username = username, password = password)
        response = requests.post(
            url = "http://localhost:4111/api/auth/token/login",
            headers = RequestSpec.base_header(),
            json = request.model_dump()
        )

        if response.status_code == 200:
            response_data = AuthLoginResponse(**response.json())
            token = response_data.token

            headers = RequestSpec.base_header()
            headers["Authorization"] = f"Bearer {token}"
            return headers
        raise Exception("Failed to authorization")

    @staticmethod
    def no_auth_header():
        return RequestSpec.base_header()

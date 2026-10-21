import requests
from src.main.api.requests.requester import Requester
from requests import Response
from src.main.api.models.create_account_response import CreateAccountResponse
from http import HTTPStatus



class CreateAccountRequester(Requester):
    def post(self, model = None) -> CreateAccountResponse | Response:
        url=f"{self.base_url}/account/create"
        response = requests.post(
            url = url,
            headers = self.headers
        )
        self.responce_specs(response)

        if response.status_code == HTTPStatus.CREATED:
            return CreateAccountResponse(**response.json())
        return response



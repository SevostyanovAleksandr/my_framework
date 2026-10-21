import requests
from src.main.api.requests.requester import Requester
from requests import Response
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response  import CreditRepayResponse
from http import HTTPStatus

class CreditRepayRequester(Requester):
    def post(self, credit_repay_request: CreditRepayRequest) -> CreditRepayResponse | Response:
        url = f'{self.base_url}/credit/repay'
        response = requests.post(
            url=url,
            json=credit_repay_request.model_dump(),
            headers=self.headers
        )
        self.responce_specs(response)
        if response.status_code == HTTPStatus.OK:
            return CreditRepayResponse(**response.json())
        return response
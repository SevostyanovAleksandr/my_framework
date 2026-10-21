from typing import Optional
import allure

from fondation.http_requester import HttpRequester
from fondation.requesters.crud_requester import CrudRequester
from models.base_model import BaseModel
from configs.config import Config



class ValidateCrudRequester(HttpRequester):
    def __init__(self, request_spec, endpoint, response_spec):
        super().__init__(request_spec, endpoint, response_spec)
        self.crud_requester = CrudRequester(
            request_spec = request_spec,
            endpoint= endpoint,
            response_spec = response_spec
        )

    def post(self, model: Optional[BaseModel] = None  ) -> BaseModel:
        respone = self.crud_requester.post(model)
        
        with allure.step(f"POST {Config.fetch("backendUrl")}{self.endpoint.value.url} Валидация модели:"):
            allure.attach(
                f"Валидация модели ответа {self.endpoint.value.response_model.__name__}"
            )

        self.response_spec(respone)
        return self.endpoint.value.response_model.model_validate(respone.json())


    def delete(self, user_id: int):
        respone = self.crud_requester.delete(user_id)
        self.response_spec(respone)
        return self.endpoint.value.response_model.model_validate(respone.json())
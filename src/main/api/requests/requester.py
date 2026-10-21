from abc import ABC, abstractmethod
from typing import Dict, Callable

from src.main.api.models.base_model import BaseModel



class Requester(ABC):
    def __init__(self, request_specs: Dict[str, str], responce_specs: Callable):
        self.headers  = request_specs["headers"]
        self.base_url = request_specs["base_url"]
        self.responce_specs = responce_specs

    @abstractmethod
    def post(model: BaseModel):...
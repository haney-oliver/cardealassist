import requests
from model.vin import VinInfo
from util.logging_utils import logger
import json

class CarAPI:
    def __init__(self, api_token: str, api_secret: str) -> None:
        self.api_token = api_token
        self.api_secret = api_secret
        self.jwt = self._login()

    def _login(self) -> str:
        return requests.post(
            "https://carapi.app/api/auth/login",
            headers={
                "accept": "text/plain; charset=utf-8",
                "Content-Type": "application/json",
            },
            json={"api_token": self.api_token, "api_secret": self.api_secret},
        ).text

    def fetch_vin_info(self, vin: str) -> VinInfo:
        url: str = f"https://carapi.app/api/vin/{vin}"
        v_info: dict =requests.get(
            url,
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {self.jwt}",
            },
        ).json()
        v_info["vin"] = vin
        return VinInfo(**v_info)

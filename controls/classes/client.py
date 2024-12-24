# -*- author: Harun Emre Tutal -*-

import requests as reqs
try:
    from config import BASE_URL
except ModuleNotFoundError:
    BASE_URL = ""

class Client:
    _client = None

    def __new__(cls):
        if cls._client is None:
            cls._client = object.__new__(cls)
        return cls._client

    def __init__(self):
        if hasattr(self, "_initialized"):
            return         
        self._initialized = True
        print("init çalıştı")
    
    def send(self, route: str, json: dict, method: str="get", url: str=BASE_URL) -> reqs.Response:
        return reqs.request(method=method,
                            url="/".join((url, route)),
                            json=json
                            )


if __name__ == "__main__":
    print(id(Client()))
    print(id(Client()))

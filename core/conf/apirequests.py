from dataclasses import dataclass
from core.conf.base_api import BaseApi
import requests
import json


@dataclass()
class Response:
    status_code: int
    as_dict: object
    headers: dict


class ApiRequests(BaseApi):

    # http_headers = BaseApi.__init__()

    def get(self, url):
        print(url)
        response = requests.get(url)
        return self.__get_responses(response)

    def post(self, url, payload):
        response = requests.post(url, data=payload, headers=super().__init__())
        return self.__get_responses(response)

    def patch(self, url, payload):
        response = requests.patch(url, data=payload, headers=super().__init__())
        return self.__get_responses(response)

    def put(self, url, payload, headers):
        response = requests.put(url, data=payload, headers=super().__init__())
        return self.__get_responses(response)

    def delete(self, url, payload, headers):
        response = requests.delete(url, data=payload, headers=super().__init__())
        return self.__get_responses(response)

    def __get_responses(self, response):
        self.status_code = response.status_code

        try:
            self.as_dict = json.dumps(response.json())
        except Exception:
            self.as_dict = {}

        self.headers = response.headers

        return Response(
            self.status_code, self.as_dict, self.headers
        )

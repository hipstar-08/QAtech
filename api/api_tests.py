from core.conf.apirequests import ApiRequests
from core.conf.base_api import BaseApi
from core.utils.fileutils import *
from core.common.constants import ApiRequestsConstants


class ApiTests(ApiRequests):
    payload_json = {
        "title": 'foo',
        "body": 'bar',
        "userId": "1",
        "id": 101
    }

    def __init__(self):
        super().__init__()

        self.base_url = ApiRequestsConstants.REQUEST_URL
        self.request = ApiRequests()

    def set_tests(self, url=''):
        return self.base_url + url

    def get_tests(self, url):
        return self.request.get(url)

    def post_tests(self, url):
        return self.request.post(url, payload=self.payload_json)


def verify_status_code(self, http_status_code):
    response = ApiTests
    assert response.status_code == http_status_code


def verify_json_body(json_file, response):
    return compareJSON(json_file, response.as_dict)

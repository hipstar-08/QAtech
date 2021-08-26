
import logging

import requests as requests
import urllib3
from core.common.constants import ApiRequestsConstants
from core.conf.config import configs

_instances = {}


class Singleton(object):
    _instances = {}
    def __new__(class_, *args, **kwargs):  # @NoSelf
        if class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]


class BaseApi(object):
    __metaclass__ = Singleton

    config = {}
    http_headers = {}
    http_body = {}

    def __init__(self):
        # logger()
        self.constant = ApiRequestsConstants

    def get_api_url(self):
        return self.config[ApiRequestsConstants.REQUEST_URL]

    def set_api_url(self, api_url):
        self.config[ApiRequestsConstants.REQUEST_URL] = api_url

    def get_http_content_type(self):
        return self.http_headers[ApiRequestsConstants.CONTENT_TYPE]

    def set_http_content_type(self, content_type):
        self.http_headers[ApiRequestsConstants.CONTENT_TYPE] = content_type

    def get_http_accept_type(self):
        return self.http_headers[ApiRequestsConstants.ACCEPT_TYPE]

    def set_http_accept_type(self, accept_type):
        self.http_headers[ApiRequestsConstants.ACCEPT_TYPE] = accept_type

    def get_http_request_body(self, content_type):
        return self.http_body

    def clear_http_request_body(self):
        self.http_body.clear()

    def clear_http_request_header(self):
        self.http_headers.clear()

    def get_response(self):
        return self.config[ApiRequestsConstants.RESP_BLOCK]

    def get_response_json(self):
        return self.config[ApiRequestsConstants.RESP_BLOCK].json()

    def http_get_response(self, api_url):
       return urllib3.PoolManager().request('GET', ApiRequestsConstants.REQUEST_URL+api_url, headers=self.http_headers)
        # self.config[ApiRequestsConstants.RESP_BLOCK] = requests.get(ApiRequestsConstants.REQUEST_URL+api_url,
        #                                                             headers = self.http_headers,
        #                                                             data=self.http_body)

    def logger(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


cs = BaseApi()
# cs.set_response()
test = cs.http_get_response('/posts')

json_resp = cs.get_response_json()
print(json_resp)

# url = cs.get_api_url()

# print(url)

# cs.config[ApiRequestsConstants.RESP_BLOCK] = test
#
# print(cs.config.items())
# print(cs.config.items())
# # print(d)

from core.common.constants import ApiRequestsConstants
from api.api_tests import *
from behave import given, when, then

api_endpoint = {}

request_json = {}
response = {}
request_headers = {}
response_headers = {}
response_codes = {}
response_body = {}
api_url = None


class Api_Steps(ApiTests):

    @given(u'Base endpoint')
    def base_case(self):
        ApiTests().set_tests()

    @given(u'Set a GET request to "{url}" endpoint')
    @given(u'Set a POST request to "{url}" endpoint')
    def set_get_request(self, url=''):
        api_endpoint['GET_URL'] = ApiTests().set_tests(url)

    @when(u'Send a "{method_type}" request to posts endpoint')
    def send_request(self, method_type):
        if method_type == 'GET':
            http_response = ApiTests().get_tests(api_endpoint['GET_URL'])
            response_codes['GET'] = http_response.status_code
            response_body['GET'] = http_response.as_dict
            response_headers['GET'] = http_response.as_dict
        elif method_type == 'POST':
            print("I am here")
            http_response = ApiTests().post_tests(api_endpoint['GET_URL'])
            response_codes['POST'] = http_response.status_code
            response_body['POST'] = http_response.as_dict
            print(response_codes['POST'])
            print(response_body['POST'])
            response_headers['POST'] = http_response.as_dict


        return http_response

    @then(u'Assert Response code "{method_type}" is "{http_status_code}"')
    def verify_http_status_code(self, method_type, http_status_code):
        if method_type == 'GET':
            response_codes['GET'] == http_status_code
        elif method_type == 'POST':
            response_codes['POST'] == http_status_code

    @then(u'Return True for Response "{method_type}" json body matches the posts file in resources')
    def verify_resp_json_body_with_resource_file(self,  method_type):
        if method_type == 'GET':
            val = compareJSON(ApiRequestsConstants.POSTS_JSON, response_body['GET'])
            assert val.__str__() == 'True'
        elif method_type == 'POST':
            val = compareJSON_single_payload(ApiTests.payload_json, response_body['POST'])
            assert val.__str__() == 'True'

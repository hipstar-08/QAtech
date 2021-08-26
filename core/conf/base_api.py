from core.common.constants import ApiRequestsConstants


class BaseApi(object):

    def __init__(self):
        self.headers = {
            ApiRequestsConstants.CONTENT_TYPE: ApiRequestsConstants.APPLICATION_JSON,
            ApiRequestsConstants.CHARSET: ApiRequestsConstants.ENCODING
        }

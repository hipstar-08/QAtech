import json
import os
import platform

from core.conf.config import configs


class GlobalConstants(object):
    drivers_path = "resources\drivers"
    PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    CHROME_DRIVER_WIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "chromedriver.exe"))
    CHROME_DRIVER_LIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "chromedriver"))
    FIREFOX_DRIVER_WIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "geckodriver.exe"))
    FIREFOX_DRIVER_LIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "geckodriver"))
    OPERA_DRIVER_WIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "operadriver.exe"))
    OPERA_DRIVER_LIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "operadriver"))
    PLATFORM_NAME = platform.system()
    SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT_DIR, os.path.join("screenshots"))


class ApiRequestsConstants(object):
    REQUEST_URL = configs['api_url']
    REQUEST_GET = 'GET'
    REQUEST_POST = 'POST'
    REQUEST_PUT = 'PUT'
    REQUEST_PATCH = 'PATCH'
    REQUEST_DELETE = 'DELETE'
    APPLICATION_JSON = 'application/json'
    CONTENT_TYPE = 'Content-Type'
    CHARSET = 'charset'
    ENCODING = 'UTF-8'
    ACCEPT_TYPE = 'Accept'
    URL_POSTS = 'posts'
    URL_COMMENTS = 'comments'
    URL_ALBUMS = 'albums'
    URL_PHOTOS = 'photos'
    URL_TODOS = 'todos'
    URL_USERS = 'users'
    RESP_BLOCK = "http_response"
    STATUS_CODE = '200'
    STATUS_CODE_400 = '400'

    PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    JSON_FOLDER_PATH = "resources\jsons"

    POSTS_JSON = os.path.join(PROJECT_ROOT_DIR, os.path.join(JSON_FOLDER_PATH, "posts.json"))
    ALBUMS_JSON = os.path.join(PROJECT_ROOT_DIR, os.path.join(JSON_FOLDER_PATH, "albums.json"))
    COMMENTS_JSON = os.path.join(PROJECT_ROOT_DIR, os.path.join(JSON_FOLDER_PATH, "comments.json"))
    PHOTOS_JSON = os.path.join(PROJECT_ROOT_DIR, os.path.join(JSON_FOLDER_PATH, "photos.json"))
    TODOS_JSON = os.path.join(PROJECT_ROOT_DIR, os.path.join(JSON_FOLDER_PATH, "todos.json"))
    USERS_JSON = os.path.join(PROJECT_ROOT_DIR, os.path.join(JSON_FOLDER_PATH, "users.json"))
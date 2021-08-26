import os
import json

from core.common.constants import *


def capture_screenshot(driver, screenshot_path=os.path.join(GlobalConstants.SCREENSHOTS_DIR, "screenshot.png")):
    driver.save_screenshot(screenshot_path)


def load_json_file(file_path):
    fh = open(file_path, 'r')
    data = json.load(fh)
    fh.close()
    return data


def sorting(json_dict):
    if isinstance(json_dict, dict):
        return sorted((key, sorting(values)) for key, values in json_dict.items())
    if isinstance(json_dict, list):
        return sorted(sorting(x) for x in json_dict)
    else:
        return json_dict


def compareJSON(json_from_file, json_from_response):
    json_file_dump = load_json_file(json_from_file)
    json_from_file_dict = json.dumps(json_file_dump)
    return sorting(json_from_file_dict) == sorting(json_from_response)


# def compareJSON_single_payload(json_from_response, post_single_payload):
#     # json_file_dump = load_json_file(json_from_file)
#     # json_from_file_dict = json.dumps(json_file_dump)
#     print(json_from_response)
#     print(post_single_payload)
#     post_single_payload_dump = json.dumps(post_single_payload)
#     print(post_single_payload_dump)
#     return sorting(post_single_payload) == sorting(json_from_response)


def compareJSON_single_payload(post_single_payload, json_from_response):
    post_single_payload_dump = json.dumps(post_single_payload)
    return sorting(post_single_payload_dump) == sorting(json_from_response)

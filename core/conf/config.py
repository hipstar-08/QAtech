import os
import json

configs = None


def load_configs():
    global configs
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')) as file_input:
        configs = json.load(file_input)


load_configs()

import os
from runpy import run_path

from statics.constants import STYLES_PATH_FULL


def valid_request_keys(keys_in: list, keys: list):
    """Check if request has all necessary keys"""
    return set(keys_in.keys()).issubset(keys)


def get_style_info(style_name: str):
    return run_path(os.path.join(STYLES_PATH_FULL.format(style_name), 'properties.py'))

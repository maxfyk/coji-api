import os
from runpy import run_path

from statics.constants import STYLE_PATH_FULL


def valid_request_keys(keys_in, keys):
    """Check if request has all necessary keys"""
    return set(keys_in.keys()).issubset(keys)


def get_style_info(style_name):
    return run_path(os.path.join(STYLE_PATH_FULL.format(style_name), 'properties.py'))

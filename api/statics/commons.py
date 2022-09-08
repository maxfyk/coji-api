import os
import dill
import sys
from runpy import run_path

from statics.constants import STYLES_PATH_FULL


def valid_request_keys(keys_in: list, keys: list):
    """Check if request has all necessary keys"""
    return set(keys_in.keys()).issubset(keys)


def get_style_info(style_name: str):
    with open(f'/app/static/styles/{style_name}/comp_properties.pickle', 'rb') as style_file:
        return dill.load(style_file)


def upd_pickled_styles():
    """Pickle style's properties.py to save on load time. TMP"""
    styles = [x[1] for x in os.walk('/app/static/styles/')][0]
    print(styles)
    for style_name in styles:
        style_module = run_path(os.path.join(STYLES_PATH_FULL.format(style_name), 'properties.py'))['style_module']

        needs_upd = True
        if os.path.isfile(f'/app/static/styles/{style_name}/comp_properties.pickle'):
            with open(f'/app/static/styles/{style_name}/comp_properties.pickle', 'rb') as style_file:
                style_module_old = dill.load(style_file)
                needs_upd = style_module['style-info'] != style_module_old['style-info']

        print(style_name, needs_upd)
        if needs_upd:
            with open(f'/app/static/styles/{style_name}/comp_properties.pickle', 'wb+') as style_file:
                dill.dump(style_module, style_file)
    print('upd_pickled_styles DONE!')
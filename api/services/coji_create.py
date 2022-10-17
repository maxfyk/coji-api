from datetime import datetime

from flask import Blueprint
from flask import jsonify
from flask import request

from modules import (
    generate_code_id,
    generate_visual_code,
)
from modules.formator import prepare_code_info
from modules.db_operations import add_new_code, get_last_code, update_code
from statics.commons import get_style_info, valid_request_keys
from statics.constants import (
    COJI_CREATE_REQUEST_KEYS,
    COJI_UPDATE_REQUEST_KEYS,
    COJI_DATA_TYPES,
    STYLES_PATH_FULL
)

coji_create_bp = Blueprint('coji-create', __name__)


@coji_create_bp.route('/create', methods=['POST'])
def coji_create():
    """Create a new code and return it as a jpeg image"""
    json_request = request.json
    print('CREATE| REQUEST', json_request)
    if not valid_request_keys(json_request, COJI_CREATE_REQUEST_KEYS):
        print('STATUS: Missing required keys')
        return jsonify(error=422, text='Missing required keys', notify_user=False), 422
    if json_request['data-type'] not in COJI_DATA_TYPES:
        print('STATUS: Unsupported type')
        return jsonify(error=415, text='Unsupported type', notify_user=False), 415

    json_request['time-created'] = json_request['time-updated'] = str(datetime.now())
    json_request['time-updated'] = str(datetime.now())

    style_name = json_request['style-info']['name']
    style_module = get_style_info(style_name)
    style_module['style-info'].update(json_request['style-info'])

    _, index = get_last_code().popitem()
    index = index['index'] + 1
    json_request['index'] = index
    char_code = generate_code_id(code_len=style_module['style-info']['total-length'],
                                 index=index)  # generate random id
    img = generate_visual_code(style_module, char_code,
                               STYLES_PATH_FULL.format(style_name))  # create image
    # add! save code to db
    new_code = prepare_code_info(json_request, char_code)
    add_new_code(new_code)
    print(new_code)
    print('STATUS: success')
    return jsonify({
        'error': False,
        'code': char_code,
        'image': img,
    }), 200


@coji_create_bp.route('/update', methods=['POST'])
def coji_update():
    """Update old code's information"""
    json_request = request.json
    print('UPDATE| REQUEST', json_request)
    if not valid_request_keys(json_request, COJI_UPDATE_REQUEST_KEYS):
        print('STATUS: Missing required keys')
        return jsonify(error=422, text='Missing required keys', notify_user=False), 422
    if json_request['data-type'] not in COJI_DATA_TYPES:
        print('STATUS: Unsupported type')
        return jsonify(error=415, text='Unsupported type', notify_user=False), 415

    json_request['time-updated'] = str(datetime.now())

    style_name = json_request['style-info']['name']
    style_module = get_style_info(style_name)
    style_module['style-info'].update(json_request['style-info'])

    code_id = json_request['code-id']
    del json_request['code-id']
    # add! save code to db
    update_code(code_id, json_request)
    print('STATUS: success')
    return jsonify({
        'error': False,
    }), 200

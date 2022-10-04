import base64

from flask import Blueprint
from flask import jsonify
from flask import request

from modules.db_operations import find_code, get_code
from modules import recognize_code
from statics.commons import (
    get_style_info,
    valid_request_keys
)
from statics.constants import (
    COJI_DECODE_REQUEST_KEYS,
    COJI_DECODE_TYPES
)

coji_decode_bp = Blueprint('coji-decode', __name__)


@coji_decode_bp.route('/decode', methods=['get', 'post'])
def coji_decode():
    """Decode and return if code exist"""
    json_request = request.json
    # add! CHECK FOR VALID IMAGE
    print('DECODE| REQUEST', json_request['decode-type'], json_request['user-id'])
    if not valid_request_keys(json_request, COJI_DECODE_REQUEST_KEYS):
        print('STATUS: Missing required keys')
        return jsonify(error=422, text='Missing required keys', notify_user=False), 422
    if json_request['decode-type'] not in COJI_DECODE_TYPES:
        print('STATUS: Unsupported type')
        return jsonify(error=415, text='Unsupported type', notify_user=False), 415

    style_name = json_request['style-info']['name']
    style_module = get_style_info(style_name)
    style_module['style-info'].update(json_request['style-info'])

    char_code = None
    if json_request['decode-type'] == 'image':
        image_str = json_request['in-data']
        if 'data:image/png' in image_str:  # if image contains a tag
            image_str = image_str.split(',')[1]

        char_code = recognize_code(image_str, style_module)  # recognize code on image
        if not char_code:
            print('STATUS: bad image')
            return jsonify(error=404, text='Code not found :(\nPlease try again!', notify_user=False), 422
        print('Code found:', char_code)
    else:
        char_code = json_request['in-data']
    char_code = 'kmfkkmlfdkafcgfd'  # FOR DEBUGGING
    code_exists = find_code(char_code)
    if code_exists is None:
        return jsonify(error=404, text='This code no longer exists!', notify_user=False), 422

    print('STATUS: success')
    print('---------------')
    return jsonify({
        'error': False,
        'code-id': char_code,
    }), 200


@coji_decode_bp.route('/get/<id>', methods=['get'])
def coji_get(id):
    """Get all the info about code by id"""
    print('GET| REQUEST', id)
    code_data = get_code(id)
    if code_data is None:
        return jsonify(error=404, data={}, notify_user=False), 422
    print('STATUS: success')
    print('---------------')
    return jsonify({
        'error': False,
        'data': code_data,
    }), 200

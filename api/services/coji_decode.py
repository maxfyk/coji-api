import base64

from flask import Blueprint
from flask import jsonify
from flask import request

from modules.recognize_code import get_prediction
from statics.commons import (
    get_style_info,
    valid_request_keys
)
from statics.constants import (
    COJI_DECODE_REQUEST_KEYS,
    COJI_DECODE_TYPES
)

coji_decode_bp = Blueprint('coji-decode', __name__)


@coji_decode_bp.route('/decode', methods=['get'])
def coji_decode():
    """Decode and return information"""
    json_request = request.json
    print('DECODE| REQUEST', json_request['decode-type'], json_request['user-id'])
    if not valid_request_keys(json_request, COJI_DECODE_REQUEST_KEYS):
        print('STATUS: Missing required keys')
        return jsonify(error=422, text='Missing required keys', notify_user=False), 422
    if json_request['decode-type'] not in COJI_DECODE_TYPES:
        print('STATUS: Unsupported type')
        return jsonify(error=415, text='Unsupported type', notify_user=False), 415

    style_name = json_request['style-info']['name']
    style_module = get_style_info(style_name)
    print('Got style')
    style_module['style-info'].update(json_request['style-info'])
    print(style_module['style-info'])

    char_code = None
    if json_request['decode-type'] == 'image':
        image_str = base64.b64decode(json_request['in-data'])
        char_code = get_prediction(image_str, style_module)  # recognize code on image
        if not char_code:
            print('STATUS: bad image')
            return jsonify(error=404, text='Code not found, bad image', notify_user=False), 422
    else:
        char_code = json_request['in-data']
    # add! lookup in db
    encoded_data = char_code
    # return data
    print('STATUS: success')
    return jsonify({
        'success': True,
        'data': encoded_data,
    }), 200

from flask import Flask, request
from flask import jsonify

from modules import generate_code_id, generate_visual_code
from statics.commons import get_style_info, valid_request_keys
from statics.constants import (
    COJI_CREATE_REQUEST_KEYS,
    COJI_DATA_TYPES,
    STYLE_PATH_FULL
)

app = Flask(__name__)


@app.route('/coji-code/create', methods=['POST'])
def coji_create():
    """Create a new coji and return it as a jpeg image"""
    json_request = request.json
    print('REQUEST', json_request)
    if not valid_request_keys(json_request, COJI_CREATE_REQUEST_KEYS):
        return jsonify(error=422, text='Missing required keys', notify_user=False), 422
    if json_request['data-type'] not in COJI_DATA_TYPES:
        return jsonify(error=415, text='Unsupported type', notify_user=False), 415

    style_name = json_request['style-info']['name']
    style_module = get_style_info(style_name)
    style_module['style_info'].update(json_request['style-info'])
    print(style_module['style_info'])
    char_code = generate_code_id(code_len=style_module['TOTAL_LENGTH'])  # generate random id
    img = generate_visual_code(style_module, char_code,
                               STYLE_PATH_FULL.format(style_name))  # create image
    # save code to db
    print('STATUS: success')
    return jsonify({
        'success': True,
        'code': char_code,
        'image': img,
    }), 200


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

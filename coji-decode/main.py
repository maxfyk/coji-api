from flask import Flask, request
from flask import jsonify

from modules import recognize_code
from statics.commons import get_style_info, valid_request_keys
from statics.constants import (
    COJI_DECODE_REQUEST_KEYS,
    COJI_DECODE_TYPES,
    STYLES_PATH_FULL
)

app = Flask(__name__)


@app.route('/coji-code/decode', methods=['get'])
def coji_decode():
    """Decode and return information"""
    json_request = request.json
    print('DECODE| REQUEST', json_request)
    if not valid_request_keys(json_request, COJI_DECODE_REQUEST_KEYS):
        print('STATUS: Missing required keys')
        return jsonify(error=422, text='Missing required keys', notify_user=False), 422
    if json_request['data-type'] not in COJI_DECODE_TYPES:
        print('STATUS: Unsupported type')
        return jsonify(error=415, text='Unsupported type', notify_user=False), 415

    style_name = json_request['styles-info']['name']
    style_module = get_style_info(style_name)
    style_module['style_info'].update(json_request['styles-info'])
    print(style_module['style_info'])

    char_code = generate_code_id(code_len=style_module['TOTAL_LENGTH'])  # generate random id
    img = generate_visual_code(style_module, char_code,
                               STYLES_PATH_FULL.format(style_name))  # create image
    # add! save code to db
    print('STATUS: success')
    return jsonify({
        'success': True,
        'code': char_code,
        'image': img,
    }), 200


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

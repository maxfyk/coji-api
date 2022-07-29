from flask import jsonify
from flask import Flask, request

from static.commons import valid_request_keys
from static.constants import (
    COJI_DATA_TYPES,
    COJI_CREATE_REQUEST_KEYS
)

app = Flask(__name__)


@app.route('/coji/create', methods=['POST'])
def coji_create():
    """Create a new coji and return it as a jpeg image"""
    json_request = request.json
    if not valid_request_keys(request.keys, COJI_CREATE_REQUEST_KEYS):
        return jsonify(error=422, text='Missing required keys'), 422
    if json_request['type'] not in COJI_DATA_TYPES:
        return jsonify(error=415, text='Unsupported type'), 415

    print(json_request['data'])
    return jsonify(**json_request), 200


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

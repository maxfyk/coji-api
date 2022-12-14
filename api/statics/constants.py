import os

# coji-create
# main
COJI_DATA_TYPES = ('text', 'url', 'file')  # 'video', 'file', 'ar'
COJI_CREATE_REQUEST_KEYS = ('in-data', 'data-type', 'user-id', 'style-info')
COJI_UPDATE_REQUEST_KEYS = ('in-data', 'data-type', 'user-id', 'code-id', 'style-info')
COJI_DB_CODE_FIELDS = ('index', 'in-data', 'data-type', 'user-id', 'style-info', 'time-created', 'time-updated')
# coji-decode
# main
COJI_DECODE_TYPES = ('image', 'keyboard')  # 'location'
COJI_DECODE_REQUEST_KEYS = ('decode-type', 'in-data', 'user-id', 'style-info')

# static
# commons
STYLES_PATH_SHORT = 'styles/{}/'
STYLES_PATH_FULL = os.path.join(os.path.dirname(os.path.abspath(__file__)), STYLES_PATH_SHORT)

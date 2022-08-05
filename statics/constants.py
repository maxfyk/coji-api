import os
# coji-create
# main
COJI_DATA_TYPES = ('text', 'url', 'image')  # 'video', 'file', 'ar'
COJI_CREATE_REQUEST_KEYS = ('in-data', 'data-type', 'user-id', 'style-info')
# static
# commons
STYLE_PATH_SHORT = 'coji-styles/{}/'
STYLE_PATH_FULL = os.path.join(os.path.dirname(os.path.abspath(__file__)), STYLE_PATH_SHORT)

style_info = {
    'name': 'geom-original',
    'size': 600,
    'rows': 4,
    'pieces-row': 4,
    'background-color': (26, 26, 26),
    'border': {
        'border-size': 15,
        'border-color': (255, 191, 0),  # 'yellow',
    }
}
model_info = {
    'settings': ['MODEL.WEIGHTS', 'output/model_final.pth', 'MODEL.ROI_HEADS.SCORE_THRESH_TEST', '0.80',
                 'MODEL.RETINANET.SCORE_THRESH_TEST', '0.80'],
    'recognition_supported': True
}

TOTAL_LENGTH = style_info['rows'] * style_info['pieces-row']
style_info['total-length'] = TOTAL_LENGTH

name_to_key = {
    'circle': 'a',
    'd-arrow': 'b',
    'e-circle': 'c',
    'e-rhombus': 'd',
    'e-square': 'e',
    'e-triangle': 'f',
    'l-arrow': 'g',
    'minus': 'h',
    'plus': 'i',
    'r-arrow': 'j',
    'rhombus': 'k',
    'square': 'l',
    'triangle': 'm',
    'u-arrow': 'n',
    'v-bar': 'o',
    'x': 'p'
}
key_to_name = {v: k for k, v in name_to_key.items()}

names = list(name_to_key.keys())
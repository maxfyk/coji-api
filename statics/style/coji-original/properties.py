style_info = {
    'name': 'coji-original',
    'size': 600,
    'rows': 3,
    'pieces-row': 3,
    'background-color': (26, 26, 26),
    'border': {
        'border-size': 15,
        'border-color': (255, 191, 0),  # 'yellow',
    }
}

model_info = {
    'settings': ['MODEL.WEIGHTS', 'output/model_final.pth', 'MODEL.ROI_HEADS.SCORE_THRESH_TEST', '0.5',
                 'MODEL.RETINANET.SCORE_THRESH_TEST', '0.5'],
    'recognition_supported': True
}
TOTAL_LENGTH = style_info['rows'] * style_info['pieces-row']
style_info['total-length'] = TOTAL_LENGTH

name_to_key = {
    'bear': 'a',
    'cat': 'b',
    'cow': 'c',
    'dog': 'd',
    'doon': 'e',
    'hamster': 'f',
    'koala': 'g',
    'lion': 'h',
    'loon': 'i',
    'monkey': 'j',
    'mouse': 'k',
    'octopus': 'l',
    'oxacea': 'm',
    'panda': 'n',
    'pig': 'o',
    'rabbit': 'p'
}

key_to_name = {v: k for k, v in name_to_key.items()}

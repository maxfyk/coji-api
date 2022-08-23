style_module = {}

style_module['style-info'] = {
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

style_module['style-info']['total-length'] = \
    style_module['style-info']['rows'] * style_module['style-info']['pieces-row']

style_module['name_to_key'] = {
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

style_module['key_to_name'] = {v: k for k, v in style_module['name_to_key'].items()}

style_module['names'] = list(style_module['name_to_key'].keys())

# MODEL INFO

style_module['model_info'] = {
    'recognition_supported': False
}

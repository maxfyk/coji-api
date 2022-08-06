TOTAL_LENGTH = 16

style_info = {
    'name': 'geom-original',
    'size': 600,
    'rows': 4,
    'pieces-row': 4,
    'total_length': TOTAL_LENGTH,
    'background-color': (26, 26, 26),
    'border': {
        'border-size': 15,
        'border-color': (255, 191, 0),  # 'yellow',
    }
}

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

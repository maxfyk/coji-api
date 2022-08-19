from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor

style_module = {}

style_module['style-info'] = {
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

style_module['style-info']['total-length'] = \
    style_module['style-info']['rows'] * style_module['style-info']['pieces-row']

style_module['name_to_key'] = {
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
style_module['key_to_name'] = {v: k for k, v in style_module['name_to_key'].items()}

style_module['names'] = list(style_module['name_to_key'].keys())

# MODEL INFO

style_module['model_info'] = {
    'settings': ['MODEL.WEIGHTS', f'''/app/statics/styles/{style_module['style-info']['name']}/model/model.pth''',
                 'MODEL.ROI_HEADS.SCORE_THRESH_TEST', '0.80',
                 'MODEL.RETINANET.SCORE_THRESH_TEST', '0.80', 'MODEL.DEVICE', 'cpu'],
    'CONFIG_FILE': f'''/app/statics/styles/{style_module['style-info']['name']}/model/{style_module['style-info']['name']}.yaml''',
    'recognition_supported': True
}

style_module['model_info']['model_cfg'] = get_cfg()
style_module['model_info']['model_cfg'].merge_from_file(style_module['model_info']['CONFIG_FILE'])
style_module['model_info']['model_cfg'].merge_from_list(style_module['model_info']['settings'])
style_module['model_info']['model_cfg'].freeze()
style_module['model_info']['predictor'] = DefaultPredictor(style_module['model_info']['model_cfg'])


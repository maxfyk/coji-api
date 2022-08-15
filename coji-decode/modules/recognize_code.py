import cv2
import numpy as np
from model_tools import setup_cfg
from detectron2.engine import DefaultPredictor


def get_matches_only(preds):
    """Sort predictions by their location and score; return classnames only"""
    pred_classes = preds.pred_classes.cpu().tolist()
    pred_scores = preds.scores.cpu().tolist()
    pred_boxes = preds.pred_boxes

    if len(pred_classes) < 16:  # style total len
        return None
    predictions = []
    for i in range(len(preds)):
        predictions.append({
            'class': pred_classes[i],
            'score': pred_scores[i],
            'box-x': pred_boxes[i][0],
            'box-y': pred_boxes[i][1],
        })
    predictions = sorted(predictions[:16], key=lambda p: (p['box-y'], p['box-x']))  # style total len
    return [p['class'] for p in predictions]


def get_prediction(image_bytes: bytes, style_module: dict):
    """Recognize code pieces on the image and return the recognized code as a string"""
    style_name = style_module['style_info']['name']

    cfg = setup_cfg(style_module['model_info'], style_name)
    predictor = DefaultPredictor(cfg)

    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(image_np, flags=1)
    predictions = predictor(img)

    pred_classes = get_matches_only(predictions["instances"])

    if pred_classes:
        name_to_key = style_module['name_to_key']
        out_code = ''.join([name_to_key[p] for p in pred_classes])
        return out_code

    return None


if __name__ == '__main__':
    style_info = {
        'style_info': {
            'name': 'geom-original',
        },
        'model_info': {
            'settings': ['MODEL.WEIGHTS', f'''../statics/styles/geom-original/model/model.pth''',
                         'MODEL.ROI_HEADS.SCORE_THRESH_TEST', '0.60',
                         'MODEL.RETINANET.SCORE_THRESH_TEST', '0.60'],
            'recognition_supported': True
        }
    }

    img = open('C:\\Users\\maxfyk\\Downloads\\photo_2022-08-12_16-24-41.jpg', 'rb')
    get_prediction(img.read(), style_info)

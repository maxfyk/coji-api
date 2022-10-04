import base64
import io
from imageio import imread

# WILL BE MOVED TO FRONT-END LATER
__all__ = ['recognize_code']


def get_matches_only(preds):
    """Sort predictions by their location and score; return classnames only"""
    pred_classes = preds.pred_classes.cpu().tolist()
    pred_scores = preds.scores.cpu().tolist()
    pred_boxes = preds.pred_boxes
    print(pred_classes)
    if len(pred_classes) < 16:  # styles total len
        return None
    predictions = []
    for i in range(len(preds)):
        predictions.append({
            'class': pred_classes[i],
            'score': pred_scores[i],
            'box-x': float(list(pred_boxes[i])[0][0]),
            'box-y': float(list(pred_boxes[i])[0][1]),
        })
    predictions = sorted(predictions[:16], key=lambda p: (p['box-y'], p['box-x']))  # styles total len
    print([p['class'] for p in predictions])
    return [p['class'] for p in predictions]


def recognize_code(image_bytes: bytes, style_module: dict):
    """Recognize code pieces on the image and return the recognized code as a string"""
    predictor = style_module['model_info']['predictor']

    img = imread(io.BytesIO(base64.b64decode(image_bytes)), pilmode='RGB')

    print('before predictor')
    predictions = predictor(img)
    print('after')
    pred_classes = get_matches_only(predictions['instances'])
    if pred_classes:
        names = style_module['names']
        name_to_key = style_module['name_to_key']
        out_code = ''.join([name_to_key[names[p]] for p in pred_classes])
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

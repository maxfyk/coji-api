from detectron2.config import get_cfg


def setup_cfg(model_info: dict, style_name: str):
    """Create configs and perform basic setups"""
    cfg = get_cfg()
    cfg.merge_from_file(f'../statics/styles/{style_name}/model/{style_name}.yaml')
    cfg.merge_from_list(model_info['settings'])
    cfg.freeze()
    return cfg

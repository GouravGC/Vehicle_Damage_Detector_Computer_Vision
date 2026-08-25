from src.model import YOLOModel


def test_model_loading():
    model = YOLOModel()
    model.load()

    assert model.is_loaded()
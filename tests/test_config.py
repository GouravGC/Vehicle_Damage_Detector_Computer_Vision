from src.config import MODEL_PATH


def test_model_path_exists():
    assert MODEL_PATH.exists()
    assert MODEL_PATH.is_file()
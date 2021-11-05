import pytest

def test_import_tensorflow() -> None:
    try:
        import tensorflow as tf
        if not tf.test.gpu_device_name():
            pytest.fail("No GPU detected")
    except Exception as e:
        pytest.fail(e)


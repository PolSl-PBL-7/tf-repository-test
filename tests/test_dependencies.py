import pytest
import sys
import os
sys.path.append(os.getenv("PYTHONPATH"))

def test_import_tensorflow() -> None:
    import tensorflow as tf

    if not tf.test.gpu_device_name():
        pytest.fail("No GPU detected")

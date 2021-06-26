try:
    import tensorflow as tf
except ImportError:
    raise ImportError('Please run "pip install -U tensorflow" to install tensorflow first for tensorflow utilities.')


def gpu_is_available():
    return len(tf.config.list_physical_devices("GPU")) > 0

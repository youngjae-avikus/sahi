from typing import Optional
from sahi.utils.file import download_from_url


class Yolov4TestConstants:
    YOLOV4_MODEL_URL = "https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights"
    YOLOV4_MODEL_PATH = "tests/data/models/yolov4/yolov4-tiny.weights"
    YOLOV4_CONFIG_URL = "https://raw.githubusercontent.com/hhk7734/tensorflow-yolov4/master/config/yolov4-tiny.cfg"
    YOLOV4_CONFIG_PATH = "tests/data/models/yolov4/yolov4-tiny.cfg"
    YOLOV4_NAMES_URL = "https://raw.githubusercontent.com/hhk7734/tensorflow-yolov4/master/test/dataset/coco.names"
    YOLOV4_NAMES_PATH = "tests/data/models/yolov4/coco.names"


def download_yolov4_model(destination_path: Optional[str] = None):

    if destination_path is None:
        destination_path = Yolov4TestConstants.YOLOV4_MODEL_PATH

    download_from_url(Yolov4TestConstants.YOLOV4_MODEL_URL, destination_path)
    download_from_url(Yolov4TestConstants.YOLOV4_CONFIG_URL, Yolov4TestConstants.YOLOV4_CONFIG_PATH)
    download_from_url(Yolov4TestConstants.YOLOV4_NAMES_URL, Yolov4TestConstants.YOLOV4_NAMES_PATH)

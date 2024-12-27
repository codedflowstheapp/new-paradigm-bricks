import logging
import numpy as np
import io
from typing import Union
from PIL import Image
from coded_flows.types import Str, PILImage, NDArray, Bytes, BytesIOType


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

coded_flows_metadata = {
    "display_name": "Read Image",
    "description": "Reading image",
    "icon": "photo-filled",
    "requirements": ["numpy", "pillow"],
    "options": [
        {
            "name": "output_type",
            "display_name": "Output Type",
            "type": "select",
            "choices": ["array", "pil", "bytes", "bytesio"],
            "default": "array",
        }
    ],
}


def read_image(path: Str, options) -> Union[PILImage, NDArray, Bytes, BytesIOType]:

    output_type = options["output_type"]

    image = Image.open(path)

    if output_type == "array":
        image = np.array(image)
    elif output_type == "bytes":
        with io.BytesIO() as buffer:
            image.save(buffer, format=image.format)
            image = buffer.getvalue()
    elif output_type == "bytesio":
        buffer = io.BytesIO()
        image.save(buffer, format=image.format)
        buffer.seek(0)
        image = buffer

    return image

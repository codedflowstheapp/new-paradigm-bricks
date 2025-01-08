from PIL import Image
import numpy as np
from io import BytesIO
from typing import Union, Tuple
from PIL import Image
from coded_flows.types import Str, PILImage, NDArray, Bytes, BytesIOType

coded_flows_metadata = {
    "display_name": "Generate RGB Channels",
    "description": "Generating image, red, green, blue (RGB) channels.",
    "icon": "photo-hexagon",
    "options": [
        {
            "name": "is_intensity",
            "display_name": "Display intensity",
            "type": "toggle",
            "default": False,
        }
    ],
}


def extract_rgb_channels(
    input_image: Union[Str, PILImage, NDArray, Bytes, BytesIOType], options
) -> Tuple[PILImage, PILImage, PILImage]:

    is_intensity = options["is_intensity"]

    # Load the image based on the input type
    if isinstance(input_image, Image.Image):
        pil_image = input_image
    elif isinstance(input_image, np.ndarray):
        pil_image = Image.fromarray(input_image)
    elif isinstance(input_image, bytes):
        pil_image = Image.open(BytesIO(input_image))
    elif isinstance(input_image, BytesIOType):
        pil_image = Image.open(input_image)
    elif isinstance(input_image, str):
        pil_image = Image.open(input_image)
    else:
        raise ValueError("Unsupported input type. Please provide a valid image input.")

    # Ensure the image is in RGB mode
    pil_image = pil_image.convert("RGB")

    # Split the image into R, G, and B channels
    r, g, b = pil_image.split()

    # Colorize each channel
    if not is_intensity:
        r = Image.merge(
            "RGB", (r, Image.new("L", r.size, 0), Image.new("L", r.size, 0))
        )
        g = Image.merge(
            "RGB", (Image.new("L", g.size, 0), g, Image.new("L", g.size, 0))
        )
        b = Image.merge(
            "RGB", (Image.new("L", b.size, 0), Image.new("L", b.size, 0), b)
        )

    return r, g, b

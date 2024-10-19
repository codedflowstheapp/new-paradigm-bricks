import logging
from coded_flows.types import Int, Str

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

coded_flows_metadata = {
    "display_name": "Generate Text",
    "description": "Generating a random text.",
    "icon": "typography",
    "options": [
        {
            "name": "is_words",
            "display_name": "Generate Words",
            "type": "toggle",
            "default": False,
        },
        {
            "name": "reference_text",
            "display_name": "Reference Words",
            "type": "textarea",
            "default": "this is default text a bit more extensive than others",
            "max_characters": 1000,
        },
    ],
}

def generate_random_text(n: Int, options) -> Str:
    """## This is a simple doc
    It was from inside the docstring...magical right?!
    ```python
    def magical_world():
        return "magic"
    ```
    """

    import random
    import string

    # Split the reference text into words
    generate_words = options["is_words"]
    reference_text = options["reference_text"]

    if generate_words:
        words = reference_text.split()

        # Ensure n is non-negative
        n = max(n, 0)

        # Generate the new text by randomly selecting words
        generated_words = [random.choice(words) for _ in range(n)]

        for word in generate_words:
            logger.info("===========>>> This is the list of words!!! <<<===========")
            logger.info(f"===========>>> {word}")
            logger.info("===========>>> End of the list <<<===========")

        # Combine the generated words into a text
        generated_text = " ".join(generated_words)
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + " "
        generated_text = "".join(random.choice(characters) for _ in range(n))

    return generated_text

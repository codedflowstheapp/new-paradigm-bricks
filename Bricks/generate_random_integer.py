from coded_flows.types import Int


coded_flows_metadata = {
    "display_name": "Generate Integer",
    "description": "Generating a random integer value.",
    "icon": "number-123",
    "options": [
        {
            "name": "min_value",
            "type": "integer",
            "step": 1,
            "max": 10,
            "min": 0,
            "default": 0,
        },
        {
            "name": "max_value",
            "type": "integer",
            "step": 1,
            "max": 200,
            "min": 0,
            "default": 100,
        },
    ],
}


def generate_random_integer(options) -> Int:
    """## This is a simple doc
    It was from inside the docstring...magical right?!
    ```python
    def magical_world():
        return "magic"
    ```
    """
    import random

    min_value = options["min_value"]
    max_value = options["max_value"]
    random_integer = random.randint(min_value, max_value)

    return random_integer

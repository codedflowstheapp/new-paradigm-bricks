from coded_flows.types import Str


coded_flows_metadata = {
    "display_name": "Concatenate",
    "description": "Concatenate two texts.",
    "icon": "font",
    "options": [{"name": "separator", "type": "input", "default": "_"}],
}


def concatenate_strings_with_separator(string1: Str, string2: Str, options) -> Str:
    """## This is a simple doc
    It was from inside the docstring...magical right?!
    ```python
    def magical_world():
        return "magic"
    ```
    """

    separator = options["separator"]
    result_string = string1 + separator + string2
    return result_string

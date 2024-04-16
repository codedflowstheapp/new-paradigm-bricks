from coded_flows.types import Int, Str


coded_flows_metadata = {
    "display_name": "Int to Str",
    "description": "Convert integer to string.",
    "icon": "typography",
}


def parse_integer_to_text(number: Int) -> Str:
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    text_representation = str(number)

    return text_representation

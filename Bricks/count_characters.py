from coded_flows.types import Str, Int


coded_flows_metadata = {
    "display_name": "Count Characters",
    "description": "count the number of characters.",
    "icon": "stopwatch-20",
}


def count_characters(text: Str) -> Int:
    char_count = len(text)
    return char_count

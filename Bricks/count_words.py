from coded_flows.types import Str, Int


coded_flows_metadata = {
    "display_name": "Count Words",
    "description": "count the number of words.",
    "icon": "number",
}


def count_words(text: Str) -> Int:
    import re

    words = re.findall(r"\w+", text)
    word_count = len(words)

    return word_count

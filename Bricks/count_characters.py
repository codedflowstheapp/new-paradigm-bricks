import logging
from coded_flows.types import Str, Int

# Configure logging
logging.basicConfig(level=logging.INFO)

coded_flows_metadata = {
    "display_name": "Count Characters",
    "description": "count the number of characters.",
    "icon": "number",
}


def count_characters(text: Str) -> Int:
    logging.info("Starting character count for input text.")
    char_count = len(text)
    logging.info("Character count completed. Total characters: %d", char_count)
    return char_count

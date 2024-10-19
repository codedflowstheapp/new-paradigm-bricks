from coded_flows.types import Str


coded_flows_metadata = {
    "display_name": "Delete File",
    "description": "Delete file.",
    "icon": "trash",
}


def delete_file(file_path: Str):
    import os

    os.remove(file_path)

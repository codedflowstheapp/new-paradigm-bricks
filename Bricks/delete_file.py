from coded_flows.types import FilePath


coded_flows_metadata = {
    "display_name": "Delete File",
    "description": "Delete file.",
    "icon": "trash-can",
}


def delete_file(file_path: FilePath):
    import os

    os.remove(file_path)

from coded_flows.types import DirectoryPath


coded_flows_metadata = {
    "display_name": "Create Folder",
    "description": "create a folder.",
    "icon": "folder",
}


def create_folder_if_not_exists(folder_path: DirectoryPath) -> DirectoryPath:
    import os

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path

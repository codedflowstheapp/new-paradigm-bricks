from coded_flows.types import FilePath


coded_flows_metadata = {
    "display_name": "Update Name",
    "description": "Update file name.",
    "icon": "pen-clip",
}


def update_file_name(old_file_path: FilePath, new_file_name: FilePath) -> FilePath:
    import os

    # Extract the directory path and the current file name
    directory_path, current_file_name = os.path.split(old_file_path)

    # Create the new file path with the updated name
    new_file_path = os.path.join(directory_path, new_file_name)

    # Rename the file with the new name
    os.rename(old_file_path, new_file_path)

    return new_file_path

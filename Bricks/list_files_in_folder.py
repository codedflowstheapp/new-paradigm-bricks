from coded_flows.types import DirectoryPath, DataRecords


coded_flows_metada = {
    "display_name": "List of files",
    "description": "List of files with there size in KB.",
    "icon": "list",
}


def list_files_in_folder(folder_path: DirectoryPath) -> DataRecords:
    """## This is a simple doc
    It was from inside the docstring...magical right?!
    ```python
    def magical_world():
        return "magic"
    ```
    """

    import os

    file_list = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            # Get the file size in kilobytes
            file_size_kb = os.path.getsize(file_path) / 1024.0

            # Create a dictionary object for each file
            file_info = {"file_name": file_name, "file_size_kb": file_size_kb}

            file_list.append(file_info)

    return file_list

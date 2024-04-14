from coded_flows.types import FilePath


coded_flows_metadata = {
    "display_name": "Move File",
    "description": "move file to a new destination.",
    "icon": "folder-tree",
}


def move_file(source_path: FilePath, destination_folder: FilePath):
    """## This is a simple doc
    It was from inside the docstring...magical right?!
    ```python
    def magical_world():
        return "magic"
    ```
    """

    import shutil

    shutil.move(source_path, destination_folder)

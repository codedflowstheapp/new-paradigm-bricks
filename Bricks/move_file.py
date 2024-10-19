from coded_flows.types import Str


coded_flows_metadata = {
    "display_name": "Move File",
    "description": "move file to a new destination.",
    "icon": "file-arrow-right",
}


def move_file(source_path: Str, destination_folder: Str):
    """## This is a simple doc
    It was from inside the docstring...magical right?!
    ```python
    def magical_world():
        return "magic"
    ```
    """

    import shutil

    shutil.move(source_path, destination_folder)

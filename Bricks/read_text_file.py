from coded_flows.types import Str


coded_flows_metadata = {
    "display_name": "Read Text File",
    "description": "Read the content of a text file and return it as a text.",
    "icon": "file-description",
}


def read_text_file(file_path: Str) -> Str:
    import os

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    # Check if the path is a directory
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"'{file_path}' is a directory, not a file.")

    # Try to open and read the file
    with open(file_path, "r") as file:
        file_content = file.read()

    # Return the content as text
    return file_content

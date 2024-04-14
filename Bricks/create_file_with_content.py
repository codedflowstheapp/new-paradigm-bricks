from coded_flows.types import FilePath, DirectoryPath, Str


coded_flows_metadata = {
    "display_name": "Create File",
    "description": "Create a text file with a text content.",
    "icon": "file-lines",
}


def create_file_with_content(
    text_content: Str, file_path: DirectoryPath, file_name: Str
) -> FilePath:
    import os

    # Ensure the directory structure exists
    os.makedirs(file_path, exist_ok=True)

    # Combine the file path and name
    file_location = os.path.join(file_path, file_name)

    # Write the text content to the file
    with open(file_location, "w") as file:
        file.write(text_content)

    return file_location

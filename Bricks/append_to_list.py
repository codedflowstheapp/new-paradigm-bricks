from coded_flows.types import List, Any


coded_flows_metadata = {
    "display_name": "Append Value to List",
    "description": "Append a value to list.",
    "icon": "row-insert-bottom",
}


def append_to_list(lst: List, value: Any) -> List:
    """## This is a simple doc
    It was from inside the docstring...magical right?!
    ```python
    def magical_world():
        return "magic"
    ```
    ![Image here](./images/imgx.jpg)
    """
    lst.append(value)
    return lst

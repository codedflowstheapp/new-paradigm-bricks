from coded_flows.types import DataRecords, Str, List


coded_flows_metadata = {
    "display_name": "Extract values list",
    "description": "Extract values of an attribute from a key-pair list.",
    "icon": "list",
}


def get_values_from_list_of_dicts(dict_list: DataRecords, key: Str) -> List:
    values_list = [d[key] for d in dict_list if key in d]
    return values_list

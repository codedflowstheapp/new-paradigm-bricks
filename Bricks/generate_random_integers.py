from coded_flows.types import Int, List


coded_flows_metadata = {
    "display_name": "Generate Integer List",
    "description": "generaye a list of random integer values.",
    "icon": "list",
}


def generate_random_integers(n: Int) -> List:
    from random import randint

    int_list = [randint(1, 100) for _ in range(n)]
    return int_list

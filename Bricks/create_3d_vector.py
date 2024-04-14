from coded_flows.types import List, NDArray


coded_flows_metadata = {
    "display_name": "Create Vector",
    "description": "Create a 3D vector.",
    "icon": "vector-square",
    "requirements": ["numpy"],
}


def create_3d_vector(list1: List, list2: List, list3: List) -> NDArray:
    import numpy as np

    vector = np.array([list1, list2, list3])
    return vector

from coded_flows.types import NDArray, Number


coded_flows_metadata = {
    "display_name": "Scalar Product",
    "description": "Scalar product of two vectors.",
    "icon": "vector-square",
    "requirements": ["numpy"],
}


def scalar_product(vector1: NDArray, vector2: NDArray) -> Number:

    import numpy as np

    product = np.dot(vector1, vector2)
    return product

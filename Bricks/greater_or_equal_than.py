from coded_flows.types import Number, Bool


coded_flows_metadata = {
    "display_name": "a ≥ b",
    "description": "Append a value to list.",
    "icon": "math-equal-greater",
}


def greater_or_equal_than(a: Number, b: Number) -> Bool:
    result = a >= b
    return result

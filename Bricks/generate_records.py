import pandas as pd
import numpy as np
import random
import ipaddress

coded_flows_metadata = {
    "display_name": "Generate Records",
    "description": "Generate various records for testing data display",
    "icon": "logs",
    "options": [
        {
            "name": "nb_records",
            "display_name": "Number of records",
            "type": "integer",
            "step": 1,
            "max": 10000,
            "min": 5,
            "default": 10,
        },
        {
            "name": "output_type",
            "display_name": "Output Type",
            "type": "select",
            "choices": ["dataframe", "np_ip_array", "geo_list", "num_list"],
            "default": "array",
        },
    ],
}


def generate_records(options):
    output = []
    num_records = options["nb_records"]
    data_type = options["output_type"]

    if not isinstance(num_records, int) or num_records <= 0:
        raise ValueError("num_records must be a positive integer.")

    if data_type == "dataframe":
        data = {
            "col1": range(num_records),
            "col2": [random.random() for _ in range(num_records)],
            "col3": [random.choice(["A", "B", "C"]) for _ in range(num_records)],
            "col4": range(num_records),
            "col5": [random.random() for _ in range(num_records)],
            "col6": [random.choice(["D", "E", "F"]) for _ in range(num_records)],
            "col7": range(num_records),
            "col8": [random.random() for _ in range(num_records)],
            "col9": [random.choice(["G", "H", "I"]) for _ in range(num_records)],
            "col10": range(num_records),
            "col11": [random.random() for _ in range(num_records)],
            "col12": [random.choice(["J", "K", "L"]) for _ in range(num_records)],
        }
        output = pd.DataFrame(data)

    elif data_type == "np_ip_array":
        ip_array = []
        for _ in range(num_records):
            # Generate random IPv4 addresses
            ip_int = random.randint(0, 2**32 - 1)
            ip_str = str(ipaddress.IPv4Address(ip_int))
            ip_array.append(ip_str)
        output = np.array(ip_array)

    elif data_type == "geo_list":
        geo_list = []
        for _ in range(num_records):
            lat = random.uniform(-90, 90)
            lon = random.uniform(-180, 180)
            geo_list.append({"latitude": lat, "longitude": lon})
        output = geo_list

    elif data_type == "num_list":
        output = [random.randint(0, 100) for _ in range(num_records)]

    return output

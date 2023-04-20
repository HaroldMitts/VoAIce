import json

def count_objects(data):
    """
    Recursively count the number of objects in a JSON data structure.
    """
    if isinstance(data, dict):
        return 1 + sum(count_objects(v) for v in data.values())
    elif isinstance(data, list):
        return sum(count_objects(v) for v in data)
    else:
        return 0

# specify the path to your JSON file
json_file_path = "voices.json"

# read the JSON file
with open(json_file_path, "r") as f:
    json_data = json.load(f)

# count the number of objects
num_objects = count_objects(json_data)

# print the result to the console
print("Number of objects in JSON file:", num_objects)

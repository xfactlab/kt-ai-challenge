import jsonlines
import re
import json
import yaml

def read_jsonlines(file_path):
    data = []
    with jsonlines.open(file_path) as reader:
        for line in reader:
            data.append(line)
    return data


class JSONLWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_json_line(self, data):
        with jsonlines.open(self.file_path, mode='a') as writer:
            writer.write(data)


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data

def get_keys(file_path):
    with open(file_path, 'r') as file:
        try:
            yaml_data = yaml.safe_load(file)
            # yaml_data now contains the parsed YAML data as a Python object
            # You can access the data using dictionary-like syntax
            # For example, if your YAML file has a key named 'foo', you can access its value like this:
            # foo_value = yaml_data['foo']
        except yaml.YAMLError as e:
            print("Error while parsing YAML file:", e)

    return yaml_data
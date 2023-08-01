import jsonlines
import re


def read_json(file_path):
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
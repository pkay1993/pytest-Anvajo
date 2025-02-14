import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union


class DataStructureDemo:
    BOUNDARY_HIGH = 100
    BOUNDARY_LOW = 0

    def __init__(self, items: Optional[List[str]] = None, data: Optional[Dict[str, Any]] = None):
        self.items = items if items else []
        self.items_backup = []
        self.data = data if data else {}

    def add_item(self, item):
        """creates a backup and appends the given item"""
        self.items_backup = self.items.copy() # Davor war backup und items die selbe Referenz
        self.items.append(item)

    def set_item(self, key, value):
        self.data[key] = (value) # String ungleich INT

    def transform_items(self, start_index: int = 0):
        result = []
        num_items = len(self.items)

        for idx, item in enumerate(self.items[start_index:], start=start_index):
            print(f"Transforming item {idx}/{num_items} ...")
            result.append(item.upper())
        return result 

    def get_evaluation(self, value):
        if value > self.BOUNDARY_HIGH:
            return "Large"
        elif value <= self.BOUNDARY_LOW:
            return "Negative"
        else:
            return "Normal"

    def write_data(self, filepath: Union[str, Path]):
        with open(filepath, 'w', encoding="utf-8") as fd:
            json.dump({"data": self.data}, fd)

    def read_data(self, filepath: Union[str, Path]):
        with open(filepath, 'r', encoding="utf-8") as fd:
            loaded_data = json.load(fd)
        self.data = loaded_data["data"]

def format_string(name, age):
        old_style = "Name: %s, Age: %d" % (name, age)
        new_style = f"Name: {name}, Age: {age}"
        return old_style, new_style

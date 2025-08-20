#!/usr/bin/python3
import json
from pathlib import Path
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = str(type(obj).__name__) + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        jsdata = {}
        for i in FileStorage.__objects:
            jsdata[i] = FileStorage.__objects[i].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(jsdata, f)

    def reload(self):
        f_path = Path(FileStorage.__file_path)
        if f_path.exists():
            with open(FileStorage.__file_path, "r") as f:
                jsdata = json.load(f)
                for i in jsdata:
                    self.new(eval(jsdata[i]["__class__"])(jsdata[i]))

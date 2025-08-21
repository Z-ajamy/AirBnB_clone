#!/usr/bin/python3
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

fs = FileStorage()
print(type(fs.reload))
file_path = "file.json"
try:
    file_path = FileStorage._FileStorage__file_path
except:
    pass
try:
    os.remove(file_path)
except:
    pass
try:
    fs._FileStorage__objects.clear()
except:
    pass

ids = []
for i in range(10):
    bm = BaseModel()
    bm.updated_at = datetime.utcnow()
    fs.new(bm)
    ids.append(bm.id)

try:
    os.remove(file_path)
except:
    pass
fs.save()

try:
    fs._FileStorage__objects.clear()
except:
    pass
fs.reload()

all_reloaded = fs.all()

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload")

for id in ids:
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing {}".format(id))

try:
    os.remove(file_path)
except Exception as e:
    pass

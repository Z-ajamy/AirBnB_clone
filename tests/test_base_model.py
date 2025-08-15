#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime

bm = BaseModel()
bm.updated_at = datetime.utcnow()
d_json = bm.to_dict()
print(type(d_json))
print(type(d_json['id']))
print(type(d_json['created_at']))
print(type(d_json['__class__']))
print(d_json['__class__'])

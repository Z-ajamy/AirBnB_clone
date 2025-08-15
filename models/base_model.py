#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        return("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        dic = self.__dict__
        dic["__clss__"] = type(self).__name__
        dic["created_at"] = datetime.isoformat(self.created_at)
        dic["updated_at"] = datetime.isoformat(self.updated_at)
        return dic

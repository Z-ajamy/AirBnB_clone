#!/usr/bin/python3
import uuid
import datetime


class BaseModel:

    def __init__(self):
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def save(self):
        self.updated_at = datetime.datetime.utcnow()

    def to_dict(self):
        dect = self.__dict__.copy()
        dect['created_at'] = self.created_at.isoformat()
        dect['updated_at'] = self.updated_at.isoformat()
        dect["__class__"] = type(self).__name__
        return dect

    def __str__(self):
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

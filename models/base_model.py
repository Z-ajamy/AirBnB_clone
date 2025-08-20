#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for i in kwargs:
                if i != "__class__":
                    if i == "created_at" or i == "updated_at":
                        date = datetime.fromisoformat(kwargs[i])
                        setattr(self, i, date)
                    else:
                        setattr(self, i, kwargs[i])
        else:
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()
    def to_dict(self):
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic



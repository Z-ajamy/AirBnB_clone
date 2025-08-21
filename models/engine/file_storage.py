#!/usr/bin/python3
"""
BaseModel class for AirBnB project
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class that defines common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initialization of the base model
        - if kwargs is not empty → recreate instance from dict
        - else → create new instance with id and timestamps
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """
        Return string representation of the instance
        Example: [BaseModel] (1234) {'id': '1234', ...}
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates `updated_at` with the current datetime
        and saves to storage
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance
        - converts datetime to ISO string
        - adds __class__ key
        """
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr

#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Initializes the BaseModel instance
        """
        self.id = str(uuid.uuid4())  # Unique ID
        self.created_at = datetime.now()  # Creation time
        self.updated_at = datetime.now()  # Last update time

    def __str__(self):
        """
        String representation of the object
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        - Adds __class__ key
        - Converts datetime attributes to ISO format strings
        """
        # Copy all attributes
        obj_dict = self.__dict__.copy()
        # Add class name
        obj_dict["__class__"] = self.__class__.__name__
        # Convert datetime objects to string in ISO format
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

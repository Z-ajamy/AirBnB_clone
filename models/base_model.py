#!/usr/bin/python3
"""Defines a BaseModel class for object modeling.

This module provides a base class that can be used as a foundation for other
model classes. It includes automatic ID generation, timestamp tracking, and
serialization capabilities for data persistence and API interactions.
"""
import uuid
from datetime import datetime


class BaseModel:
    """A base model class that provides common functionality for data objects.
    
    This class serves as a foundation for other model classes by providing
    automatic unique ID generation, creation and update timestamp tracking,
    string representation, and dictionary serialization capabilities.
    
    Attributes:
        id (str): A unique identifier generated using UUID4.
        created_at (datetime): Timestamp when the object was created (UTC).
        updated_at (datetime): Timestamp when the object was last updated (UTC).
    
    Examples:
        >>> base = BaseModel()
        >>> print(base.id)  # Will print a UUID string
        >>> print(base.created_at)  # Will print creation timestamp
        >>> base_dict = base.to_dict()
        >>> print(base_dict['__class__'])  # Will print 'BaseModel'
    """
    
    def __init__(self):
        """Initialize a new BaseModel instance.
        
        Creates a new instance with a unique UUID4 identifier and sets both
        created_at and updated_at timestamps to the current UTC time.
        
        Args:
            None
        
        Returns:
            None
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def __str__(self):
        """Return a string representation of the BaseModel instance.
        
        Creates a formatted string containing the class name, ID, and all
        instance attributes in dictionary format.
        
        Returns:
            str: A formatted string in the format "[ClassName] (id) {attributes_dict}"
        
        Examples:
            >>> base = BaseModel()
            >>> str(base)
            '[BaseModel] (12345678-1234-5678-9abc-123456789abc) {...}'
        """
        return("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))
    
    def save(self):
        """Update the updated_at timestamp to the current UTC time.
        
        This method is typically called when the object has been modified
        and needs to reflect the time of the last update.
        
        Args:
            None
        
        Returns:
            None
        
        Examples:
            >>> base = BaseModel()
            >>> original_time = base.updated_at
            >>> base.save()
            >>> # base.updated_at is now more recent than original_time
        """
        self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        """Convert the BaseModel instance to a dictionary representation.
        
        Creates a dictionary containing all instance attributes with datetime
        objects converted to ISO format strings and the class name added as
        a special '__class__' key.
        
        Returns:
            dict: A dictionary containing all instance attributes with:
                - All original attributes as key-value pairs
                - '__class__' key with the class name as value
                - 'created_at' and 'updated_at' as ISO format strings
        
        Examples:
            >>> base = BaseModel()
            >>> result = base.to_dict()
            >>> print(result['__class__'])  # 'BaseModel'
            >>> print(type(result['created_at']))  # <class 'str'>
            >>> # created_at and updated_at are ISO formatted strings
        
        Note:
            The datetime objects are converted to ISO format strings to ensure
            JSON serialization compatibility.
        """
        dic = self.__dict__.copy()
        dic["__class__"] = str(type(self).__name__)
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic

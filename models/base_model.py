#!/usr/bin/python3
"""
BaseModel Module for HBNB Project.

This module defines the BaseModel class which serves as the foundation for all
model classes in the HBNB (Holberton BnB) project. It provides common attributes
and methods that are inherited by all other model classes.

The BaseModel class handles:
- Unique ID generation for each instance
- Timestamp management for creation and updates
- Serialization and deserialization of instances
- Integration with the storage system

Classes:
    BaseModel: Base class for all model objects in the HBNB project.

Example:
    Creating a new BaseModel instance:
        >>> from models.base_model import BaseModel
        >>> model = BaseModel()
        >>> print(model.id)
        f47ac10b-58cc-4372-a567-0e02b2c3d479
        >>> model.save()
        >>> print(model.updated_at)
        2023-01-01 12:30:45.123456

Author: HBNB Development Team
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """
    Base class for all model objects in the HBNB project.
    
    This class defines common attributes and methods that are shared across
    all model classes. It provides functionality for unique identification,
    timestamp management, serialization, and storage integration.
    
    Every instance automatically gets:
    - A unique UUID as an identifier
    - Creation and update timestamps
    - Registration with the storage system (for new instances)
    
    Attributes:
        id (str): Unique identifier for the instance, generated using UUID4.
        created_at (datetime): Timestamp when the instance was created.
        updated_at (datetime): Timestamp when the instance was last modified.
        
    Example:
        Creating a new instance:
        >>> model = BaseModel()
        >>> print(type(model.id))
        <class 'str'>
        >>> print(type(model.created_at))
        <class 'datetime.datetime'>
        
        Creating from dictionary:
        >>> data = {
        ...     'id': '1234-5678',
        ...     'created_at': '2023-01-01T12:00:00',
        ...     'updated_at': '2023-01-01T12:30:00',
        ...     'custom_attr': 'value'
        ... }
        >>> model = BaseModel(**data)
        >>> print(model.custom_attr)
        value
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance.
        
        This constructor can initialize an instance in two ways:
        1. From keyword arguments (typically from a dictionary representation)
        2. As a completely new instance with generated UUID and current timestamps
        
        When initializing from kwargs, datetime strings are automatically converted
        to datetime objects. The '__class__' key is ignored to prevent conflicts.
        
        For new instances (no kwargs), the instance is automatically registered
        with the storage system.
        
        Args:
            *args: Variable length argument list (currently unused).
            **kwargs: Arbitrary keyword arguments containing attribute data.
                     Expected keys may include:
                     - id (str): Unique identifier
                     - created_at (str): ISO format datetime string
                     - updated_at (str): ISO format datetime string
                     - Any other custom attributes
        
        Returns:
            None
            
        Example:
            New instance:
            >>> model = BaseModel()
            >>> isinstance(model.id, str)
            True
            >>> isinstance(model.created_at, datetime)
            True
            
            From dictionary:
            >>> data = {'id': '123', 'created_at': '2023-01-01T00:00:00'}
            >>> model = BaseModel(**data)
            >>> model.id
            '123'
            >>> model.created_at.year
            2023
            
        Note:
            - The '__class__' key in kwargs is automatically ignored
            - Datetime strings in 'created_at' and 'updated_at' are converted to datetime objects
            - New instances are automatically added to storage, recreated instances are not
        """
        if kwargs:
            for i in kwargs:
                if i == "__class__":
                    continue
                elif i == "created_at" or i == "updated_at":
                    date = datetime.fromisoformat(kwargs[i])
                    setattr(self, i, date)
                else:
                    setattr(self, i, kwargs[i])
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
    
            models.storage.new(self)
            
    def __str__(self):
        """
        Return string representation of the BaseModel instance.
        
        This method provides a human-readable string representation of the instance
        in the format: [ClassName] (id) {dictionary_representation}
        
        Returns:
            str: Formatted string containing class name, id, and all attributes.
            
        Example:
            >>> model = BaseModel()
            >>> print(model)
            [BaseModel] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {'id': 'f47ac10b...', 'created_at': datetime.datetime(...), 'updated_at': datetime.datetime(...)}
            
            >>> user = User()
            >>> user.name = "John"
            >>> print(user)
            [User] (12345678-1234-1234-1234-123456789012) {'id': '12345678...', 'created_at': datetime.datetime(...), 'updated_at': datetime.datetime(...), 'name': 'John'}
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        Update the instance and save it to storage.
        
        This method updates the 'updated_at' timestamp to the current UTC time
        and triggers the storage system to persist all changes to the storage backend.
        
        The method should be called whenever the instance is modified to ensure
        the timestamp reflects the latest change and the data is persisted.
        
        Returns:
            None
            
        Example:
            >>> model = BaseModel()
            >>> old_time = model.updated_at
            >>> # ... make some changes to the model ...
            >>> model.name = "Updated Name"
            >>> model.save()
            >>> model.updated_at > old_time
            True
            
            >>> # Storage is automatically updated
            >>> # The instance can now be retrieved with latest changes
            
        Note:
            - Always updates the 'updated_at' timestamp to current UTC time
            - Triggers storage.save() to persist changes across all objects
            - Should be called after any modifications to maintain data consistency
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()
        
    def to_dict(self):
        """
        Convert the instance to a dictionary representation.
        
        This method creates a dictionary containing all instance attributes
        with datetime objects converted to ISO format strings. It also adds
        a '__class__' key containing the class name for identification.
        
        This dictionary format is suitable for:
        - JSON serialization
        - Recreating instances using the constructor
        - API responses
        - Data storage and transmission
        
        Returns:
            dict: Dictionary containing all instance attributes with:
                  - All original attributes as key-value pairs
                  - '__class__' key with the class name as value
                  - 'created_at' and 'updated_at' as ISO format strings
                  
        Example:
            >>> model = BaseModel()
            >>> model.name = "Test Model"
            >>> model.number = 42
            >>> model_dict = model.to_dict()
            >>> print(model_dict['__class__'])
            'BaseModel'
            >>> print(type(model_dict['created_at']))
            <class 'str'>
            >>> print(model_dict['name'])
            'Test Model'
            >>> print(model_dict['number'])
            42
            
            >>> # Dictionary can be used to recreate the instance
            >>> new_model = BaseModel(**model_dict)
            >>> new_model.id == model.id
            True
            >>> new_model.name == model.name
            True
            
        Note:
            - Creates a copy of __dict__ to avoid modifying the original
            - Datetime objects are converted to ISO format strings
            - The '__class__' key is added for class identification
            - All custom attributes are preserved in their original form
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic

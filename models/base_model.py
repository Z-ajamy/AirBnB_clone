#!/usr/bin/python3
"""
base_model.py

This module defines the BaseModel class, which serves as a base class for other
models. It includes unique ID generation, timestamp management, and dictionary
representation.

Examples:
    >>> base = BaseModel()
    >>> base_dict = base.to_dict()
    >>> isinstance(base_dict, dict)
    True
    >>> base.save()
    >>> base.updated_at > base.created_at
    True
    >>> base_dict['created_at'] != base_dict['updated_at']
    True
"""

import uuid
import datetime


class BaseModel:
    """A base class that defines common attributes and methods
        for other models.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The timestamp when the instance was created.
        updated_at (datetime): The timestamp when the instance
            was last updated.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance, setting its ID and timestamps.

        If keyword arguments are provided, they are used to set the instance
        attributes. The 'created_at' and 'updated_at' attributes are parsed
            from ISO format strings if provided.

        Args:
            *args: Variable length argument list.
            **kwargs: Keyword arguments that initialize instance attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == 'created_at':
                    setattr(self, 'created_at', datetime.datetime.
                            strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                elif k == 'updated_at':
                    setattr(self, 'updated_at', datetime.datetime.
                            strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, k, v)

    def save(self):
        """Update the `updated_at` timestamp to the current time."""
        self.updated_at = datetime.datetime.utcnow()

    def to_dict(self):
        """Convert the instance attributes to a dictionary format.

        Returns:
            dict: A dictionary containing all instance attributes, including
                the class name.

        Examples:
            >>> base = BaseModel()
            >>> base_dict = base.to_dict()
            >>> base_dict['__class__']
            'BaseModel'
            >>> 'id' in base_dict
            True
            >>> 'created_at' in base_dict
            True
            >>> 'updated_at' in base_dict
            True
            >>> isinstance(base_dict['created_at'], str)
            True
            >>> isinstance(base_dict['updated_at'], str)
            True
        """
        dect = self.__dict__.copy()
        dect['created_at'] = self.created_at.isoformat()
        dect['updated_at'] = self.updated_at.isoformat()
        dect["__class__"] = type(self).__name__
        return dect

    def __str__(self):
        """Return a string representation of the instance.

        Returns:
            str: A string describing the instance, including its class name,
                ID, and attributes.

    Examples:
        >>> base = BaseModel()
        >>> str(base)  # doctest: +ELLIPSIS
        "[BaseModel] (...) {'id': ..., 'created_at': ..., 'updated_at':...}"
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

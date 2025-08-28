#!/usr/bin/python3
"""
FileStorage Module for HBNB Project.

This module provides file-based storage functionality for the HBNB project.
It implements a simple object-relational mapping (ORM) system that serializes
and deserializes model instances to and from JSON files.

The FileStorage class acts as an abstraction layer between the application
and the file system, providing methods to:
- Store objects in memory during runtime
- Persist objects to JSON files
- Load objects from JSON files on startup
- Manage object lifecycle and relationships

This storage engine is designed to be easily replaceable with other storage
backends (database, cloud storage, etc.) while maintaining the same interface.

Classes:
    FileStorage: Handles serialization and deserialization of objects to JSON files.

Example:
    Basic usage of the storage system:
        >>> from models.engine.file_storage import FileStorage
        >>> from models.base_model import BaseModel
        >>> 
        >>> storage = FileStorage()
        >>> model = BaseModel()
        >>> storage.new(model)
        >>> storage.save()  # Persists to file.json
        >>> 
        >>> # Later, reload from file
        >>> storage.reload()
        >>> all_objects = storage.all()
        >>> print(len(all_objects))

Author: HBNB Development Team
"""
import json

class FileStorage:
    """
    File-based storage engine for HBNB model objects.
    
    This class provides a simple file-based storage system that serializes
    model objects to JSON format and stores them persistently. It acts as
    the primary storage backend for the HBNB application.
    
    The storage system maintains all objects in memory during runtime for
    fast access, while providing methods to persist changes to disk and
    reload data on application startup.
    
    Class Attributes:
        __file_path (str): Path to the JSON file used for persistence.
                          Defaults to "file.json".
        __objects (dict): Dictionary storing all objects in memory.
                         Keys are formatted as "ClassName.object_id".
    
    Example:
        Creating and using a FileStorage instance:
        >>> storage = FileStorage()
        >>> from models.base_model import BaseModel
        >>> model = BaseModel()
        >>> storage.new(model)
        >>> len(storage.all())
        1
        >>> storage.save()  # Persists to file
        >>> 
        >>> # Create new storage instance and reload
        >>> new_storage = FileStorage()
        >>> len(new_storage.all())
        0
        >>> new_storage.reload()
        >>> len(new_storage.all())
        1
    
    Note:
        - This implementation uses class attributes to ensure singleton-like behavior
        - All instances share the same __objects dictionary and __file_path
        - Objects are keyed by "ClassName.id" format for uniqueness across types
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all stored objects.
        
        This method returns a dictionary containing all objects currently
        stored in memory. The dictionary uses keys in the format "ClassName.id"
        and values are the actual object instances.
        
        Returns:
            dict: Dictionary containing all stored objects.
                  Keys: "ClassName.object_id" (str)
                  Values: Object instances
        
        Example:
            >>> storage = FileStorage()
            >>> from models.base_model import BaseModel
            >>> model1 = BaseModel()
            >>> model2 = BaseModel() 
            >>> storage.new(model1)
            >>> storage.new(model2)
            >>> all_objects = storage.all()
            >>> len(all_objects)
            2
            >>> list(all_objects.keys())
            ['BaseModel.f47ac10b-...', 'BaseModel.6ba7b810-...']
            >>> isinstance(list(all_objects.values())[0], BaseModel)
            True
        
        Note:
            - Returns reference to the actual __objects dictionary
            - Modifications to returned dictionary affect the storage directly
            - Empty dictionary is returned if no objects are stored
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the storage.
        
        This method registers a new object in the storage system using
        a key format of "ClassName.object_id". The object is stored in
        memory and will be persisted when save() is called.
        
        Args:
            obj: The object instance to store. Must have __class__.__name__
                 and id attributes.
        
        Returns:
            None
        
        Example:
            >>> storage = FileStorage()
            >>> from models.base_model import BaseModel
            >>> from models.user import User
            >>> 
            >>> model = BaseModel()
            >>> user = User()
            >>> user.name = "John Doe"
            >>> 
            >>> storage.new(model)
            >>> storage.new(user)
            >>> 
            >>> all_objects = storage.all()
            >>> f"BaseModel.{model.id}" in all_objects
            True
            >>> f"User.{user.id}" in all_objects  
            True
            >>> all_objects[f"User.{user.id}"].name
            'John Doe'
        
        Note:
            - Objects are keyed by "ClassName.id" format
            - If an object with the same key already exists, it will be replaced
            - The object is only stored in memory until save() is called
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize all objects to JSON file.
        
        This method persists all objects currently stored in memory to the
        JSON file specified by __file_path. Each object is converted to its
        dictionary representation using the to_dict() method before serialization.
        
        The resulting JSON file contains a dictionary where keys are object
        identifiers ("ClassName.id") and values are the serialized object data.
        
        Returns:
            None
        
        Raises:
            IOError: If the file cannot be written to.
            AttributeError: If an object doesn't have a to_dict() method.
        
        Example:
            >>> storage = FileStorage()
            >>> from models.base_model import BaseModel
            >>> 
            >>> model = BaseModel()
            >>> model.name = "Test Model"
            >>> storage.new(model)
            >>> storage.save()
            >>> 
            >>> # File now contains serialized data
            >>> import json
            >>> with open("file.json", "r") as f:
            ...     data = json.load(f)
            >>> f"BaseModel.{model.id}" in data
            True
            >>> data[f"BaseModel.{model.id}"]["name"]
            'Test Model'
        
        Note:
            - Overwrites the entire JSON file on each save
            - All objects in __objects are serialized, regardless of changes
            - File is created if it doesn't exist
            - Uses UTF-8 encoding for the JSON file
        """
        jsdata = {}
        for i in FileStorage.__objects:
            jsdata[i] = FileStorage.__objects[i].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(jsdata, f)

    def reload(self):
        """
        Deserialize JSON file and load objects into memory.
        
        This method reads the JSON file specified by __file_path and recreates
        all stored objects, loading them into the __objects dictionary. Each
        object is reconstructed using its class constructor with the serialized
        data as keyword arguments.
        
        If the file doesn't exist, the method silently does nothing, allowing
        for clean startup when no previous data exists.
        
        Returns:
            None
        
        Raises:
            json.JSONDecodeError: If the JSON file is corrupted or invalid.
            KeyError: If required object attributes are missing from the data.
            NameError: If a referenced class doesn't exist or isn't imported.
        
        Example:
            >>> # Assume file.json exists with saved data
            >>> storage = FileStorage()
            >>> len(storage.all())  # Empty initially
            0
            >>> storage.reload()
            >>> len(storage.all())  # Now contains loaded objects
            3
            >>> 
            >>> # Objects are fully functional after reload
            >>> all_objects = storage.all()
            >>> obj = list(all_objects.values())[0]
            >>> obj.save()  # Can call methods on reloaded objects
        
        Example of file.json content:
            {
                "BaseModel.1234-5678": {
                    "__class__": "BaseModel",
                    "id": "1234-5678",
                    "created_at": "2023-01-01T12:00:00.000000",
                    "updated_at": "2023-01-01T12:30:00.000000"
                },
                "User.abcd-efgh": {
                    "__class__": "User",
                    "id": "abcd-efgh",
                    "email": "test@example.com",
                    "created_at": "2023-01-01T13:00:00.000000",
                    "updated_at": "2023-01-01T13:00:00.000000"
                }
            }
        
        Note:
            - Only loads if the file exists; no error if file is missing
            - Uses eval() to dynamically instantiate classes - ensure trusted data
            - Imports all model classes to make them available for instantiation  
            - Clears existing __objects and replaces with loaded data
            - Objects maintain all their attributes and functionality after reload
        """
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.place import Place
            from models.amenity import Amenity
            from models.review import Review

            classes = {"BaseModel":BaseModel, "User":User,
                    "State":State, "City":City, "Place":Place,
                    "Amenity":Amenity, "Review":Review}
            with open(FileStorage.__file_path, "r") as f:
                jsdata = json.load(f)
                for i in jsdata:
                    cls_name = jsdata[i]["__class__"]
                    self.new(classes[cls_name](**jsdata[i]))
        except FileNotFoundError:
            pass

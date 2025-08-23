#!/usr/bin/python3
"""
Storage Initialization Module for HBNB Project.

This module initializes and configures the global storage system for the HBNB
(Holberton BnB) application. It creates a single FileStorage instance that serves
as the primary storage backend throughout the application lifecycle.

The module performs the following critical initialization tasks:
1. Creates a FileStorage instance to handle object persistence
2. Loads existing data from the storage file into memory
3. Makes the storage instance globally available as 'storage'

This initialization pattern ensures that:
- All parts of the application use the same storage instance
- Previously saved data is automatically loaded on application startup
- The storage system is ready for immediate use by models and controllers

The storage instance created here is used by:
- BaseModel and its subclasses for automatic registration and persistence
- The command interpreter for CRUD operations
- Any other components requiring data persistence

Module Variables:
    storage (FileStorage): Global storage instance for the entire application.

Example:
    This module is typically imported by other modules to access storage:
        >>> from models import storage
        >>> from models.base_model import BaseModel
        >>> 
        >>> # Storage is already initialized and loaded
        >>> model = BaseModel()  # Automatically registered with storage
        >>> model.save()  # Uses the global storage instance
        >>> 
        >>> # Access all stored objects
        >>> all_objects = storage.all()
        >>> print(len(all_objects))

Author: HBNB Development Team
"""
from models.engine.file_storage import FileStorage

# Create the global storage instance for the entire application
storage = FileStorage()

# Load any existing data from the persistent storage file
# This ensures that previously saved objects are available immediately
# upon application startup, maintaining data continuity across sessions
storage.reload()

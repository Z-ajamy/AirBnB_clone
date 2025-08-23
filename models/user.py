#!/usr/bin/python3
"""
User Model Module for HBNB Project.

This module defines the User class which represents user entities in the
HBNB (Holberton BnB) application. The User class extends BaseModel to inherit
common functionality while adding user-specific attributes.

The User model is designed to store essential user information including
authentication credentials and personal details. It integrates seamlessly
with the storage system and command interpreter.

Classes:
    User: Model class representing a user in the HBNB system.

Example:
    Creating and managing User instances:
        >>> from models.user import User
        >>> user = User()
        >>> user.email = "john@example.com"
        >>> user.first_name = "John"
        >>> user.last_name = "Doe"
        >>> user.password = "secure123"
        >>> user.save()
        >>> print(user)
        [User] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {...}

Author: HBNB Development Team
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    User model class for the HBNB application.
    
    This class represents a user entity in the HBNB system, extending BaseModel
    to inherit common functionality like unique ID generation, timestamps, and
    storage integration. The User class adds specific attributes related to
    user authentication and personal information.
    
    The class is designed to work with the HBNB command interpreter and storage
    system, allowing users to be created, updated, displayed, and deleted through
    various interfaces.
    
    Attributes:
        email (str): User's email address. Defaults to empty string.
                    Used for authentication and communication.
        password (str): User's password. Defaults to empty string.
                       Used for authentication (should be hashed in production).
        first_name (str): User's first name. Defaults to empty string.
                         Used for personalization and display purposes.
        last_name (str): User's last name. Defaults to empty string.
                        Used for personalization and display purposes.
    
    Inherited Attributes:
        id (str): Unique identifier inherited from BaseModel.
        created_at (datetime): Creation timestamp inherited from BaseModel.
        updated_at (datetime): Last update timestamp inherited from BaseModel.
    
    Example:
        Creating a new user:
        >>> user = User()
        >>> user.email = "alice@example.com"
        >>> user.password = "mypassword123"
        >>> user.first_name = "Alice"
        >>> user.last_name = "Smith"
        >>> user.save()
        >>> print(f"User {user.first_name} {user.last_name} created with ID: {user.id}")
        User Alice Smith created with ID: f47ac10b-58cc-4372-a567-0e02b2c3d479
        
        Creating from dictionary (useful for deserialization):
        >>> user_data = {
        ...     'id': '1234-5678-9012',
        ...     'email': 'bob@example.com',
        ...     'first_name': 'Bob',
        ...     'last_name': 'Johnson',
        ...     'password': 'secret456',
        ...     'created_at': '2023-01-01T12:00:00.000000',
        ...     'updated_at': '2023-01-01T12:00:00.000000'
        ... }
        >>> user = User(**user_data)
        >>> print(user.email)
        bob@example.com
        >>> print(user.first_name)
        Bob
        
        Using with command interpreter:
        (hbnb) create User
        f47ac10b-58cc-4372-a567-0e02b2c3d479
        (hbnb) update User f47ac10b-58cc-4372-a567-0e02b2c3d479 email "user@example.com"
        (hbnb) update User f47ac10b-58cc-4372-a567-0e02b2c3d479 first_name "John"
        (hbnb) show User f47ac10b-58cc-4372-a567-0e02b2c3d479
        [User] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {'id': 'f47ac10b...', 'email': 'user@example.com', 'first_name': 'John', ...}
        
        Converting to dictionary:
        >>> user = User()
        >>> user.email = "test@example.com"
        >>> user.first_name = "Test"
        >>> user_dict = user.to_dict()
        >>> print(user_dict['__class__'])
        'User'
        >>> print(user_dict['email'])
        'test@example.com'
        >>> print(user_dict['first_name'])
        'Test'
    
    Note:
        - All string attributes default to empty strings, not None
        - Password storage should implement proper hashing in production environments
        - Email validation should be implemented at the application level
        - The class inherits all BaseModel methods (save, to_dict, __str__, etc.)
        - Instances are automatically registered with the storage system when created
        - Supports both direct instantiation and dictionary-based initialization
    
    Security Considerations:
        - Passwords are stored as plain text in this implementation
        - Consider implementing password hashing (bcrypt, scrypt, etc.) for production
        - Email addresses should be validated and sanitized
        - Personal information should be handled according to privacy regulations
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

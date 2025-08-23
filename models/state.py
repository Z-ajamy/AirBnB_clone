#!/usr/bin/python3
"""
State Model Module for HBNB Project.

This module defines the State class which represents geographical state or
province entities in the HBNB (Holberton BnB) application. The State class
extends BaseModel to inherit common functionality while adding state-specific
attributes for location-based services.

States serve as geographical containers in the HBNB system hierarchy:
State -> City -> Place, allowing for organized location-based searches
and categorization of rental properties.

The State model integrates with the storage system and command interpreter
to provide full CRUD functionality for managing geographical regions.

Classes:
    State: Model class representing a state/province in the HBNB system.

Example:
    Creating and managing State instances:
        >>> from models.state import State
        >>> state = State()
        >>> state.name = "California"
        >>> state.save()
        >>> print(state)
        [State] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {'id': 'f47ac10b...', 'name': 'California', ...}

Author: HBNB Development Team
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    State model class for the HBNB application.
    
    This class represents a geographical state or province entity in the HBNB
    system, extending BaseModel to inherit common functionality like unique ID
    generation, timestamps, and storage integration. The State class is designed
    to be part of the location hierarchy in the application.
    
    States are typically used to organize cities and places geographically,
    enabling location-based searches and filtering in the rental platform.
    In the HBNB system hierarchy: State contains Cities, which contain Places.
    
    The class works seamlessly with the HBNB command interpreter and storage
    system, allowing states to be created, updated, displayed, and deleted
    through various interfaces.
    
    Attributes:
        name (str): The name of the state or province. Defaults to empty string.
                   This is the primary identifying attribute for the state.
                   Examples: "California", "New York", "Texas", "Ontario", etc.
    
    Inherited Attributes:
        id (str): Unique identifier inherited from BaseModel.
        created_at (datetime): Creation timestamp inherited from BaseModel.
        updated_at (datetime): Last update timestamp inherited from BaseModel.
    
    Example:
        Creating a new state:
        >>> state = State()
        >>> state.name = "Florida"
        >>> state.save()
        >>> print(f"State '{state.name}' created with ID: {state.id}")
        State 'Florida' created with ID: f47ac10b-58cc-4372-a567-0e02b2c3d479
        
        Creating multiple states:
        >>> states = []
        >>> for state_name in ["California", "Texas", "New York"]:
        ...     state = State()
        ...     state.name = state_name
        ...     state.save()
        ...     states.append(state)
        >>> print(f"Created {len(states)} states")
        Created 3 states
        
        Creating from dictionary (useful for deserialization):
        >>> state_data = {
        ...     'id': '1234-5678-9012',
        ...     'name': 'Washington',
        ...     'created_at': '2023-01-01T12:00:00.000000',
        ...     'updated_at': '2023-01-01T12:00:00.000000'
        ... }
        >>> state = State(**state_data)
        >>> print(state.name)
        Washington
        >>> print(state.id)
        1234-5678-9012
        
        Using with command interpreter:
        (hbnb) create State
        f47ac10b-58cc-4372-a567-0e02b2c3d479
        (hbnb) update State f47ac10b-58cc-4372-a567-0e02b2c3d479 name "Nevada"
        (hbnb) show State f47ac10b-58cc-4372-a567-0e02b2c3d479
        [State] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {'id': 'f47ac10b...', 'name': 'Nevada', ...}
        (hbnb) all State
        ["[State] (f47ac10b...) {...}", "[State] (6ba7b810...) {...}"]
        
        Using dot notation with command interpreter:
        (hbnb) State.create()
        a1b2c3d4-e5f6-7890-1234-567890abcdef
        (hbnb) State.all()
        ["[State] (a1b2c3d4...) {...}"]
        (hbnb) State.show("a1b2c3d4-e5f6-7890-1234-567890abcdef")
        [State] (a1b2c3d4-e5f6-7890-1234-567890abcdef) {'id': 'a1b2c3d4...', 'name': '', ...}
        (hbnb) State.update("a1b2c3d4-e5f6-7890-1234-567890abcdef", "name", "Oregon")
        (hbnb) State.count()
        1
        
        Converting to dictionary:
        >>> state = State()
        >>> state.name = "Alaska"
        >>> state_dict = state.to_dict()
        >>> print(state_dict['__class__'])
        'State'
        >>> print(state_dict['name'])
        'Alaska'
        >>> print('created_at' in state_dict)
        True
        >>> print('updated_at' in state_dict)
        True
    
    Note:
        - The name attribute defaults to an empty string, not None
        - States are typically created before cities and places in the hierarchy
        - The class inherits all BaseModel methods (save, to_dict, __str__, etc.)
        - Instances are automatically registered with the storage system when created
        - Supports both direct instantiation and dictionary-based initialization
        - State names should be unique within the application for consistency
    
    Usage in Location Hierarchy:
        The State class is part of a geographical hierarchy:
        - State (this class) - represents states/provinces/regions
        - City (contains reference to State) - represents cities within states  
        - Place (contains reference to City) - represents rental properties in cities
        
        This hierarchy enables:
        - Geographic filtering of search results
        - Organized location-based navigation
        - Hierarchical address representation
        - Regional analytics and reporting
    
    Data Validation Considerations:
        - State names should be validated for uniqueness at the application level
        - Consider implementing name length limits for database compatibility
        - State names should be properly capitalized and formatted
        - International state/province names should be handled appropriately
    """

    name = ""

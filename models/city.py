#!/usr/bin/python3
"""
City Model Module for HBNB Project.

This module defines the City class which represents city entities in the
HBNB (Holberton BnB) application. The City class extends BaseModel to inherit
common functionality while adding city-specific attributes for location-based
services and geographical organization.

Cities serve as intermediate geographical containers in the HBNB system hierarchy:
State -> City -> Place. This allows for organized location-based searches,
hierarchical address representation, and regional categorization of rental
properties within specific urban areas.

The City model maintains a relationship with State entities through the state_id
foreign key, enabling proper geographical organization and location-based queries.

Classes:
    City: Model class representing a city in the HBNB system.

Example:
    Creating and managing City instances:
        >>> from models.city import City
        >>> from models.state import State
        >>> 
        >>> # First create a state
        >>> state = State()
        >>> state.name = "California"
        >>> state.save()
        >>> 
        >>> # Then create a city in that state
        >>> city = City()
        >>> city.name = "San Francisco"
        >>> city.state_id = state.id
        >>> city.save()
        >>> print(city)
        [City] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {'name': 'San Francisco', 'state_id': '...', ...}

Author: HBNB Development Team
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    City model class for the HBNB application.
    
    This class represents a city entity in the HBNB system, extending BaseModel
    to inherit common functionality like unique ID generation, timestamps, and
    storage integration. The City class serves as an intermediate level in the
    geographical hierarchy between State and Place entities.
    
    Cities are associated with states through a foreign key relationship and
    serve as containers for rental places. This hierarchical organization
    enables efficient location-based searches, geographical filtering, and
    structured address representation in the rental platform.
    
    The class integrates seamlessly with the HBNB command interpreter and storage
    system, allowing cities to be created, updated, displayed, and deleted
    through various interfaces while maintaining referential relationships.
    
    Attributes:
        state_id (str): Foreign key reference to the State this city belongs to.
                       Defaults to empty string. Should contain the UUID of a
                       valid State instance to maintain referential integrity.
        name (str): The name of the city. Defaults to empty string.
                   This is the primary identifying attribute for the city.
                   Examples: "San Francisco", "New York", "Austin", "Miami", etc.
    
    Inherited Attributes:
        id (str): Unique identifier inherited from BaseModel.
        created_at (datetime): Creation timestamp inherited from BaseModel.
        updated_at (datetime): Last update timestamp inherited from BaseModel.
    
    Example:
        Creating a city with state relationship:
        >>> from models.state import State
        >>> from models.city import City
        >>> 
        >>> # Create parent state first
        >>> state = State()
        >>> state.name = "Texas"
        >>> state.save()
        >>> 
        >>> # Create city within the state
        >>> city = City()
        >>> city.name = "Austin"
        >>> city.state_id = state.id
        >>> city.save()
        >>> print(f"City '{city.name}' created in state ID: {city.state_id}")
        City 'Austin' created in state ID: f47ac10b-58cc-4372-a567-0e02b2c3d479
        
        Creating multiple cities in the same state:
        >>> state = State()
        >>> state.name = "California"
        >>> state.save()
        >>> 
        >>> cities = ["Los Angeles", "San Diego", "Sacramento"]
        >>> for city_name in cities:
        ...     city = City()
        ...     city.name = city_name
        ...     city.state_id = state.id
        ...     city.save()
        >>> print(f"Created {len(cities)} cities in California")
        Created 3 cities in California
        
        Creating from dictionary (useful for deserialization):
        >>> city_data = {
        ...     'id': '1234-5678-9012',
        ...     'name': 'Chicago',
        ...     'state_id': 'abcd-efgh-ijkl',
        ...     'created_at': '2023-01-01T12:00:00.000000',
        ...     'updated_at': '2023-01-01T12:00:00.000000'
        ... }
        >>> city = City(**city_data)
        >>> print(city.name)
        Chicago
        >>> print(city.state_id)
        abcd-efgh-ijkl
        
        Using with command interpreter:
        (hbnb) create City
        f47ac10b-58cc-4372-a567-0e02b2c3d479
        (hbnb) update City f47ac10b-58cc-4372-a567-0e02b2c3d479 name "Boston"
        (hbnb) update City f47ac10b-58cc-4372-a567-0e02b2c3d479 state_id "state-uuid-here"
        (hbnb) show City f47ac10b-58cc-4372-a567-0e02b2c3d479
        [City] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {'id': 'f47ac10b...', 'name': 'Boston', 'state_id': 'state-uuid-here', ...}
        (hbnb) all City
        ["[City] (f47ac10b...) {...}", "[City] (6ba7b810...) {...}"]
        
        Using dot notation with command interpreter:
        (hbnb) City.create()
        a1b2c3d4-e5f6-7890-1234-567890abcdef
        (hbnb) City.all()
        ["[City] (a1b2c3d4...) {...}"]
        (hbnb) City.show("a1b2c3d4-e5f6-7890-1234-567890abcdef")
        [City] (a1b2c3d4-e5f6-7890-1234-567890abcdef) {'id': 'a1b2c3d4...', 'name': '', 'state_id': '', ...}
        (hbnb) City.update("a1b2c3d4-e5f6-7890-1234-567890abcdef", "name", "Portland")
        (hbnb) City.count()
        1
        
        Converting to dictionary:
        >>> city = City()
        >>> city.name = "Seattle"
        >>> city.state_id = "washington-state-uuid"
        >>> city_dict = city.to_dict()
        >>> print(city_dict['__class__'])
        'City'
        >>> print(city_dict['name'])
        'Seattle'
        >>> print(city_dict['state_id'])
        'washington-state-uuid'
        >>> print('created_at' in city_dict)
        True
        
        Querying cities by state (conceptual example):
        >>> from models import storage
        >>> all_objects = storage.all()
        >>> california_cities = []
        >>> for obj_key, obj in all_objects.items():
        ...     if obj.__class__.__name__ == 'City' and obj.state_id == california_state_id:
        ...         california_cities.append(obj)
        >>> print(f"Found {len(california_cities)} cities in California")
    
    Note:
        - Both name and state_id attributes default to empty strings, not None
        - state_id should reference a valid State instance for data integrity
        - Cities are typically created after their parent state exists
        - The class inherits all BaseModel methods (save, to_dict, __str__, etc.)
        - Instances are automatically registered with the storage system when created
        - Supports both direct instantiation and dictionary-based initialization
        - City names should be unique within a state for consistency
    
    Usage in Location Hierarchy:
        The City class operates in the middle tier of the geographical hierarchy:
        
        State (parent) -> City (this class) -> Place (child)
        
        This hierarchy enables:
        - State-based city filtering and organization
        - City-based place categorization
        - Hierarchical address representation (State, City, Place)
        - Geographic search optimization
        - Regional analytics and reporting at city level
        - Location-based service delivery
    
    Relationship Management:
        Foreign Key Relationship:
        - state_id links to State.id
        - Establishes parent-child relationship
        - Enables geographical organization
        - Supports location-based queries
        
        Child Relationships:
        - Places reference cities through city_id foreign key
        - Enables nested location searches
        - Supports hierarchical data retrieval
    
    Data Validation Considerations:
        - state_id should be validated to ensure referenced State exists
        - City names should be unique within the same state
        - Consider implementing name length limits for database compatibility
        - City names should be properly capitalized and formatted
        - Orphaned cities (invalid state_id) should be handled gracefully
        - International city names should be supported appropriately
    
    Performance Considerations:
        - Indexing on state_id recommended for efficient queries
        - Consider caching frequently accessed state-city relationships
        - Batch operations for multiple cities in the same state
        - Optimize queries that traverse the State-City-Place hierarchy
    """

    state_id = ""
    name = ""

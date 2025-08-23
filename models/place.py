#!/usr/bin/python3
"""
Place Model Module for HBNB Project.

This module defines the Place class which represents rental properties in the
HBNB (Holberton BnB) application. The Place class is the core entity of the
rental platform, extending BaseModel to inherit common functionality while
providing comprehensive property management capabilities.

Places are the central focus of the HBNB platform, representing actual rental
properties that users can book. They integrate with multiple other entities:
- Geographic hierarchy: State -> City -> Place
- User relationships: property owners and renters
- Feature associations: amenities and services
- Review system: guest feedback and ratings

The Place model provides complete property information including location,
capacity, pricing, amenities, and descriptive details necessary for a
comprehensive rental platform experience.

Classes:
    Place: Model class representing a rental property in the HBNB system.

Example:
    Creating and managing Place instances:
        >>> from models.place import Place
        >>> from models.city import City
        >>> from models.user import User
        >>> 
        >>> # Create dependencies first
        >>> owner = User()
        >>> owner.email = "owner@example.com"
        >>> owner.save()
        >>> 
        >>> city = City()
        >>> city.name = "San Francisco"
        >>> city.save()
        >>> 
        >>> # Create the place
        >>> place = Place()
        >>> place.name = "Cozy Downtown Apartment"
        >>> place.city_id = city.id
        >>> place.user_id = owner.id
        >>> place.number_rooms = 2
        >>> place.price_by_night = 150
        >>> place.save()

Author: HBNB Development Team
"""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place model class for the HBNB application.
    
    This class represents a rental property in the HBNB system, serving as the
    core entity of the rental platform. Places extend BaseModel to inherit
    common functionality while providing comprehensive property management
    capabilities including location, capacity, pricing, and feature information.
    
    The Place class integrates with multiple other entities in the system:
    - Geographic relationships through city_id (City -> State hierarchy)
    - User relationships through user_id (property owner)
    - Feature associations through amenity_ids (available amenities)
    - Review connections (guest feedback system)
    
    Places are designed to provide complete property information necessary
    for users to make informed booking decisions, including detailed
    descriptions, capacity limitations, pricing, exact location, and
    available amenities.
    
    Attributes:
        city_id (str): Foreign key reference to the City where this place is located.
                      Defaults to empty string. Should contain the UUID of a
                      valid City instance for proper geographical organization.
        user_id (str): Foreign key reference to the User who owns this property.
                      Defaults to empty string. Should contain the UUID of a
                      valid User instance representing the property owner.
        name (str): The name or title of the place. Defaults to empty string.
                   This is the primary display name for the property listing.
                   Examples: "Cozy Downtown Apartment", "Luxury Beach House",
                   "Historic City Loft", "Mountain Retreat Cabin".
        description (str): Detailed description of the place. Defaults to empty string.
                          Contains comprehensive information about the property,
                          including features, location highlights, and guest amenities.
        number_rooms (int): Number of rooms in the place. Defaults to 0.
                           Represents total rooms available for guest use,
                           typically bedrooms but may include living areas.
        number_bathrooms (int): Number of bathrooms in the place. Defaults to 0.
                               Represents total bathroom facilities available
                               to guests during their stay.
        max_guest (int): Maximum number of guests allowed. Defaults to 0.
                        Defines the occupancy limit for the property,
                        important for booking validation and pricing.
        price_by_night (int): Price per night in the platform's base currency.
                             Defaults to 0. Represents the nightly rate for
                             booking this property.
        latitude (float): Geographic latitude coordinate. Defaults to 0.0.
                         Used for mapping, location-based searches, and
                         distance calculations. Range: -90.0 to 90.0.
        longitude (float): Geographic longitude coordinate. Defaults to 0.0.
                          Used for mapping, location-based searches, and
                          distance calculations. Range: -180.0 to 180.0.
        amenity_ids (list): List of Amenity IDs associated with this place.
                           Defaults to empty list. Contains UUIDs of Amenity
                           instances representing features available at this property.
    
    Inherited Attributes:
        id (str): Unique identifier inherited from BaseModel.
        created_at (datetime): Creation timestamp inherited from BaseModel.
        updated_at (datetime): Last update timestamp inherited from BaseModel.
    
    Example:
        Creating a complete place listing:
        >>> from models.place import Place
        >>> from models.city import City
        >>> from models.user import User
        >>> from models.amenity import Amenity
        >>> 
        >>> # Create dependencies
        >>> owner = User()
        >>> owner.email = "host@example.com"
        >>> owner.first_name = "Alice"
        >>> owner.last_name = "Johnson"
        >>> owner.save()
        >>> 
        >>> city = City()
        >>> city.name = "New York"
        >>> city.save()
        >>> 
        >>> wifi = Amenity()
        >>> wifi.name = "WiFi"
        >>> wifi.save()
        >>> 
        >>> pool = Amenity()
        >>> pool.name = "Pool"
        >>> pool.save()
        >>> 
        >>> # Create the place
        >>> place = Place()
        >>> place.name = "Manhattan Luxury Apartment"
        >>> place.description = "Beautiful 2-bedroom apartment in the heart of Manhattan with stunning city views."
        >>> place.city_id = city.id
        >>> place.user_id = owner.id
        >>> place.number_rooms = 2
        >>> place.number_bathrooms = 2
        >>> place.max_guest = 4
        >>> place.price_by_night = 250
        >>> place.latitude = 40.7589
        >>> place.longitude = -73.9851
        >>> place.amenity_ids = [wifi.id, pool.id]
        >>> place.save()
        >>> print(f"Created place: {place.name} for ${place.price_by_night}/night")
        Created place: Manhattan Luxury Apartment for $250/night
        
        Creating from dictionary (useful for deserialization):
        >>> place_data = {
        ...     'id': '1234-5678-9012',
        ...     'name': 'Beach House Paradise',
        ...     'city_id': 'city-uuid-here',
        ...     'user_id': 'user-uuid-here',
        ...     'description': 'Stunning beachfront property with ocean views',
        ...     'number_rooms': 3,
        ...     'number_bathrooms': 2,
        ...     'max_guest': 6,
        ...     'price_by_night': 300,
        ...     'latitude': 25.7617,
        ...     'longitude': -80.1918,
        ...     'amenity_ids': ['wifi-uuid', 'pool-uuid', 'parking-uuid'],
        ...     'created_at': '2023-01-01T12:00:00.000000',
        ...     'updated_at': '2023-01-01T12:00:00.000000'
        ... }
        >>> place = Place(**place_data)
        >>> print(f"{place.name} - {place.number_rooms} rooms, ${place.price_by_night}/night")
        Beach House Paradise - 3 rooms, $300/night
        >>> print(f"Location: ({place.latitude}, {place.longitude})")
        Location: (25.7617, -80.1918)
        >>> print(f"Amenities: {len(place.amenity_ids)} available")
        Amenities: 3 available
        
        Using with command interpreter:
        (hbnb) create Place
        f47ac10b-58cc-4372-a567-0e02b2c3d479
        (hbnb) update Place f47ac10b-58cc-4372-a567-0e02b2c3d479 name "Cozy Cabin"
        (hbnb) update Place f47ac10b-58cc-4372-a567-0e02b2c3d479 price_by_night 120
        (hbnb) update Place f47ac10b-58cc-4372-a567-0e02b2c3d479 number_rooms 1
        (hbnb) update Place f47ac10b-58cc-4372-a567-0e02b2c3d479 max_guest 2
        (hbnb) show Place f47ac10b-58cc-4372-a567-0e02b2c3d479
        [Place] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {'id': 'f47ac10b...', 'name': 'Cozy Cabin', 'price_by_night': 120, 'number_rooms': 1, 'max_guest': 2, ...}
        
        Using dot notation with command interpreter:
        (hbnb) Place.create()
        a1b2c3d4-e5f6-7890-1234-567890abcdef
        (hbnb) Place.all()
        ["[Place] (a1b2c3d4...) {...}"]
        (hbnb) Place.show("a1b2c3d4-e5f6-7890-1234-567890abcdef")
        [Place] (a1b2c3d4-e5f6-7890-1234-567890abcdef) {'id': 'a1b2c3d4...', 'name': '', 'city_id': '', ...}
        (hbnb) Place.update("a1b2c3d4-e5f6-7890-1234-567890abcdef", "name", "Downtown Studio")
        (hbnb) Place.count()
        1
        
        Converting to dictionary:
        >>> place = Place()
        >>> place.name = "Riverside Cottage"
        >>> place.number_rooms = 2
        >>> place.price_by_night = 180
        >>> place.amenity_ids = ["wifi-id", "parking-id"]
        >>> place_dict = place.to_dict()
        >>> print(place_dict['__class__'])
        'Place'
        >>> print(place_dict['name'])
        'Riverside Cottage'
        >>> print(place_dict['number_rooms'])
        2
        >>> print(place_dict['amenity_ids'])
        ['wifi-id', 'parking-id']
        
        Searching places by criteria (conceptual examples):
        >>> from models import storage
        >>> all_objects = storage.all()
        >>> 
        >>> # Find places in a specific city
        >>> city_places = []
        >>> target_city_id = "sf-city-uuid"
        >>> for obj_key, obj in all_objects.items():
        ...     if obj.__class__.__name__ == 'Place' and obj.city_id == target_city_id:
        ...         city_places.append(obj)
        >>> print(f"Found {len(city_places)} places in the city")
        >>> 
        >>> # Find places within price range
        >>> affordable_places = []
        >>> max_price = 200
        >>> for obj_key, obj in all_objects.items():
        ...     if (obj.__class__.__name__ == 'Place' and 
        ...         obj.price_by_night > 0 and obj.price_by_night <= max_price):
        ...         affordable_places.append(obj)
        >>> print(f"Found {len(affordable_places)} places under ${max_price}/night")
        >>> 
        >>> # Find places with specific capacity
        >>> large_places = []
        >>> min_guests = 6
        >>> for obj_key, obj in all_objects.items():
        ...     if obj.__class__.__name__ == 'Place' and obj.max_guest >= min_guests:
        ...         large_places.append(obj)
        >>> print(f"Found {len(large_places)} places for {min_guests}+ guests")
    
    Note:
        - String attributes default to empty strings, not None
        - Numeric attributes default to 0 or 0.0, representing unset values
        - amenity_ids is a list that defaults to empty list
        - Foreign keys (city_id, user_id) should reference valid existing entities
        - Coordinates should be valid latitude/longitude values for mapping
        - Price should be positive for active listings
        - Capacity values should be realistic and positive
    
    Relationships in the HBNB System:
        Geographic Hierarchy:
        State -> City -> Place (this class)
        - place.city_id -> City.id
        - City.state_id -> State.id
        - Enables location-based searches and organization
        
        User Ownership:
        User -> Place (this class)
        - place.user_id -> User.id
        - Establishes property ownership
        - Enables owner-based property management
        
        Amenity Associations:
        Place (this class) <-> Amenity (many-to-many)
        - place.amenity_ids contains list of Amenity.id values
        - Enables feature-based searches and property descriptions
        - Supports flexible amenity assignment
        
        Review Connections:
        Place (this class) <- Review
        - Review.place_id -> Place.id
        - Enables guest feedback and rating systems
        - Supports property quality assessment
    
    Business Logic Considerations:
        Pricing Strategy:
        - price_by_night should be positive for active listings
        - Consider dynamic pricing based on demand, season, events
        - Support for different currency representations
        - Discount and promotion handling
        
        Capacity Management:
        - max_guest should not exceed reasonable limits
        - Consider relationship between rooms and guest capacity
        - Implement occupancy validation for bookings
        - Handle special accommodation requests
        
        Location Accuracy:
        - Latitude/longitude should be accurate for mapping
        - Consider privacy implications of exact coordinates
        - Implement location-based search algorithms
        - Support proximity searches and distance calculations
        
        Amenity Management:
        - Validate amenity_ids reference existing Amenity instances
        - Support dynamic amenity updates
        - Consider amenity categories and groupings
        - Implement amenity-based filtering and search
    
    Data Validation Guidelines:
        Required Fields Validation:
        - name should not be empty for active listings
        - city_id should reference valid City instance
        - user_id should reference valid User instance
        - price_by_night should be positive for bookings
        
        Numeric Constraints:
        - number_rooms: positive integer, reasonable maximum
        - number_bathrooms: positive integer or zero
        - max_guest: positive integer, correlate with room count
        - price_by_night: positive integer, reasonable range
        
        Geographic Constraints:
        - latitude: -90.0 to 90.0 degrees
        - longitude: -180.0 to 180.0 degrees
        - Coordinates should be within city boundaries
        
        List Validation:
        - amenity_ids: should contain valid Amenity UUIDs
        - Prevent duplicate amenity IDs in the list
        - Validate amenity existence before assignment
    
    Performance Optimization:
        Search Optimization:
        - Index on city_id for location-based queries
        - Index on price_by_night for price range searches
        - Index on max_guest for capacity-based filtering
        - Compound indexes for common search combinations
        
        Geographic Queries:
        - Spatial indexing for latitude/longitude searches
        - Efficient proximity and distance calculations
        - Geospatial query optimization
        
        Amenity Relationships:
        - Optimize many-to-many amenity queries
        - Cache frequently accessed amenity combinations
        - Efficient amenity-based filtering algorithms
    """
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

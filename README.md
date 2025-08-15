# 0x00. AirBnB clone - The console

## Project Overview

This project is the first step towards building a full web application: an AirBnB clone. The console is a command interpreter that allows you to manage AirBnB objects through a command-line interface. This foundational piece will be used throughout the subsequent projects to handle HTML/CSS templating, database storage, API development, and front-end integration.

## Description

The console application provides a simple command-line interface to:
- Create new objects (User, State, City, Place, etc.)
- Retrieve objects from files or databases
- Perform operations on objects (count, compute stats, etc.)
- Update attributes of objects
- Destroy objects
- Store and persist objects to a JSON file

This project implements the fundamental concepts of object-oriented programming, serialization/deserialization, and file storage that form the backbone of the complete AirBnB clone application.

## Command Interpreter

### How to Start

To start the console, navigate to the project directory and run:

```bash
$ ./console.py
```

Or alternatively:

```bash
$ python3 console.py
```

You should see the prompt `(hbnb)` indicating that the console is ready to accept commands.

### How to Use

The console supports two modes:

#### Interactive Mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) quit
$
```

#### Non-Interactive Mode
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Available Commands

| Command | Description | Usage |
|---------|-------------|--------|
| `create` | Creates a new instance of a class | `create <class_name>` |
| `show` | Displays string representation of an instance | `show <class_name> <id>` |
| `destroy` | Deletes an instance based on class name and id | `destroy <class_name> <id>` |
| `all` | Displays all instances of a class or all instances | `all` or `all <class_name>` |
| `update` | Updates an instance based on class name and id | `update <class_name> <id> <attribute> "<value>"` |
| `count` | Counts the number of instances of a class | `<class_name>.count()` |
| `quit` | Exits the console | `quit` |
| `EOF` | Exits the console (Ctrl+D) | `EOF` |
| `help` | Shows help information | `help` or `help <command>` |

### Classes

The following classes are available:
- `BaseModel`: Base class for all other classes
- `User`: User information
- `State`: State information
- `City`: City information  
- `Amenity`: Amenity information
- `Place`: Place information
- `Review`: Review information

### Examples

#### Creating Objects
```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) create User
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
```

#### Showing Objects
```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

#### Displaying All Objects
```bash
(hbnb) all
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]

(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```

#### Updating Objects
```bash
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```

#### Alternative Syntax
The console also supports alternative method call syntax:
```bash
(hbnb) User.count()
2
(hbnb) User.all()
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
```

#### Destroying Objects
```bash
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```

## Project Structure

```
airbnb_clone/
├── console.py          # Main console application
├── models/            # Directory containing all model classes
│   ├── __init__.py
│   ├── base_model.py  # BaseModel class
│   ├── user.py        # User class
│   ├── state.py       # State class
│   ├── city.py        # City class
│   ├── amenity.py     # Amenity class
│   ├── place.py       # Place class
│   ├── review.py      # Review class
│   └── engine/        # Storage engine
│       ├── __init__.py
│       └── file_storage.py
├── tests/             # Unit tests
└── README.md          # This file
```

## Storage

All objects are stored in a JSON file (`file.json`) using the FileStorage class. The storage system handles:
- Serialization of objects to JSON format
- Deserialization of JSON data back to objects
- Automatic saving and loading of data
- Object persistence between console sessions

## Testing

To run the unit tests:

```bash
# Run all tests
$ python3 -m unittest discover tests

# Run specific test file
$ python3 -m unittest tests/test_models/test_base_model.py

# Run specific test class
$ python3 -m unittest tests.test_models.test_base_model.TestBaseModel

# Run with verbose output
$ python3 -m unittest discover tests -v
```

## Requirements

- Python 3.8.5 or higher
- All files should be executable
- Code should follow PEP 8 style guidelines
- All modules, classes, and functions must have proper documentation

## Installation

1. Clone the repository:
```bash
$ git clone https://github.com/your-username/AirBnB_clone.git
```

2. Navigate to the project directory:
```bash
$ cd AirBnB_clone
```

3. Make the console executable:
```bash
$ chmod +x console.py
```

4. Run the console:
```bash
$ ./console.py
```

## Author

**Abd_al-rahman Ajamy**  
📧 Email: [abdorahman0283@gmail.com](mailto:abdorahman0283@gmail.com)

## License

This project is part of the ALX Software Engineering program.

## Acknowledgments

- ALX Africa
- Holberton School
- All contributors and reviewers

---

*This project is the foundation for a complete web application that will include HTML/CSS templating, database storage, API development, and front-end integration in subsequent phases.*

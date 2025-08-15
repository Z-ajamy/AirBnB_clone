# 0x00. AirBnB Clone - The Console

## Table of Contents
* [Introduction](#introduction)
* [Environment](#environment)
* [Installation](#installation)
* [Usage](#usage)
* [Testing](#testing)
* [Authors](#authors)

## Introduction

This project is a team effort to build a clone of [AirBnB](https://www.airbnb.com/). The first step in this project is to create a command interpreter to manage the backend of the AirBnB clone. This console will allow us to create, update, retrieve, and delete different objects, simulating the backend functionality of the AirBnB website.

The console performs the following tasks:
* Create a new object
* Retrieve an object from a file
* Perform operations on objects
* Destroy an object

### Storage

All classes are managed by the `Storage` engine in the `FileStorage` class, which handles the serialization and deserialization of JSON files to persist the objects.

## Environment

The project is developed and tested in the following environment:

<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Ubuntu"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="Bash"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="Python"></a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Vim"></a> <!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="VSCode"></a> <!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="Git"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="GitHub"></a>

* **Style Guidelines:**
  * [pycodestyle (version 2.8.*)](https://pypi.org/project/pycodestyle/)
  * [PEP8](https://pep8.org/)

All development and testing were conducted on an Ubuntu 20.04 LTS operating system using Python 3.8.5. Editors used include VIM, VSCode, and Emacs. Version control is managed with Git.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/AirBnB_clone.git
   cd AirBnB_clone
   ```

2. **Make the Console Executable**
   ```sh
   chmod +x console.py
   ```

### Execution

You can run the console in either interactive or non-interactive mode.

**Interactive Mode:**
```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) quit
$
```

**Non-interactive Mode:**
```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Usage

Start the console in interactive mode:
```sh
$ ./console.py
(hbnb)
```

Use `help` to see the available commands:
```sh
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

Quit the console:
```sh
(hbnb) quit
$
```

### Commands

The commands are displayed in the following format:
*Command / usage / example with output*

**Create**
```sh
create <class>
```
Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file `file.json`.
```sh
(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
```

**Show**
```sh
show <class> <id>
```
Displays the string representation of an instance based on the class name and id.
```sh
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```

**Destroy**
```sh
destroy <class> <id>
```
Deletes an instance of a given class with a given ID and updates `file.json`.
```sh
(hbnb) create User
0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) destroy User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) show User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
** no instance found **
(hbnb)
```

**All**
```sh
all [<class>]
```
Prints all string representations of all instances or instances of a specified class.
```sh
(hbnb) create BaseModel
e45ddda9-eb80-4858-99a9-226d4f08a629
(hbnb) all BaseModel
["[BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) [BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) {'id': '4c8f7ebc-257f-4ed1-b26b-e7aace459897', 'created_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447155), 'updated_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447257), 'name': 'My First Model', 'my_number': 89}"]
```

**Count**
```sh
count <class>
```
Prints the number of instances of a given class.
```sh
(hbnb) create City
4e01c33e-2564-42c2-b61c-17e512898bad
(hbnb) create City
e952b772-80a5-41e9-b728-6bc4dc5c21b4
(hbnb) count City
2
(hbnb)
```

**Update**
```sh
update <class> <id> <attribute name> "<attribute value>"
```
Updates an instance based on the class name, id, and kwargs passed, and updates `file.json`.

## Testing

All tests are defined in the `tests` folder.

### Documentation

* **Modules:**
  ```sh
  python3 -c 'print(__import__("my_module").__doc__)'
  ```

* **Classes:**
  ```sh
  python3 -c 'print(__import__("my_module").MyClass.__doc__)'
  ```

* **Functions (inside and outside

 a class):**
  ```sh
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  ```

  and

  ```sh
  python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
  ```

### Python Unit Tests

* **unittest module**
* **File extension:** `.py`
* **Files and folders start with:** `test_`
* **Organization:** for `models/base.py`, unit tests in: `tests/test_models/test_base.py`
* **Execution command:**
  ```sh
  python3 -m unittest discover tests
  ```

  or:

  ```sh
  python3 -m unittest tests/test_models/test_base.py
  ```

### Running tests in interactive mode

```sh
echo "python3 -m unittest discover tests" | bash
```

### Running tests in non-interactive mode

To run the tests in non-interactive mode and discover all the tests, use the command:

```sh
python3 -m unittest discover tests
```

## Authors

<details>
  <summary>Abd_al-rahman Ajamy</summary>
  <ul>
    <li><a href="https://www.github.com/Z-ajamy">GitHub</a></li>
    <li><a href="abdorahman0283@gmail.com">Email</a></li>
  </ul>
</details>

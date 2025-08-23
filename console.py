#!/usr/bin/python3
"""
HBNB Command Interpreter Module.

This module provides a command-line interpreter for the HBNB (Holberton BnB) project.
It allows users to interact with various model objects through a command-line interface,
providing functionality to create, show, destroy, update, and list objects.

The interpreter supports both direct command input and dot notation for method calls
(e.g., User.all(), BaseModel.show("id"), etc.).

Classes:
    HBNBCommand: Main command interpreter class that extends cmd.Cmd.

Example:
    To run the interpreter:
        $ python3 console.py
        (hbnb) help
        (hbnb) create User
        (hbnb) show User 1234-1234-1234
        (hbnb) quit

Author: HBNB Development Team
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


from models import storage

import re
import shlex
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB project.
    
    This class provides a command-line interface for managing HBNB objects.
    It extends the cmd.Cmd class to provide interactive command processing
    with support for creating, reading, updating, and deleting model instances.
    
    The interpreter supports two command formats:
    1. Standard format: command class_name [arguments]
    2. Dot notation: ClassName.method([arguments])
    
    Attributes:
        dict_of_classes (dict): Dictionary mapping class names to class objects.
        prompt (str): Command prompt displayed to the user.
    
    Example:
        >>> interpreter = HBNBCommand()
        >>> interpreter.cmdloop()
        (hbnb) create User
        f47ac10b-58cc-4372-a567-0e02b2c3d479
        (hbnb) User.all()
        ["{'id': 'f47ac10b...', 'created_at': '2023-01-01T00:00:00', ...}"]
        (hbnb) quit
    """

    dict_of_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }


    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit command to exit the program.
        
        This method handles the 'quit' command which terminates the command
        interpreter and returns control to the calling environment.
        
        Args:
            line (str): Command line input (unused for quit command).
            
        Returns:
            bool: Always returns True to signal interpreter termination.
            
        Example:
            (hbnb) quit
            $
        """
        return True

    def do_EOF(self, line):
        """
        Handle End-Of-File (EOF) signal.
        
        This method handles the EOF signal (Ctrl+D on Unix systems) to
        gracefully exit the command interpreter. It provides the same
        functionality as the quit command.
        
        Args:
            line (str): Command line input (unused for EOF handling).
            
        Returns:
            bool: Always returns True to signal interpreter termination.
            
        Example:
            (hbnb) <Ctrl+D>
            $
        """
        return True

    def emptyline(self):
        """
        Handle empty line input.
        
        This method overrides the default behavior when an empty line is entered.
        Instead of repeating the last command (default cmd.Cmd behavior), it does
        nothing and returns to the prompt.
        
        Returns:
            None
            
        Example:
            (hbnb) 
            (hbnb) 
        """
        pass


    def default(self, line):
        """
        Handle unrecognized commands and dot notation syntax.
        
        This method processes commands that don't match standard command methods.
        It specifically handles dot notation syntax like ClassName.method(args)
        and translates them to appropriate method calls.
        
        Args:
            line (str): The complete command line input.
            
        Returns:
            None or result of delegated method call.
            
        Raises:
            No explicit exceptions, but prints error messages for invalid syntax.
            
        Example:
            (hbnb) User.all()
            ["{'id': '1234', ...}"]
            (hbnb) User.show("1234")
            <User: (1234) {'id': '1234', ...}>
            (hbnb) User.destroy("1234")
            (hbnb) User.count()
            5
            
        Note:
            Supports the following dot notation methods:
            - ClassName.all()
            - ClassName.count()
            - ClassName.show("id")
            - ClassName.destroy("id")
            - ClassName.update("id", "attr_name", "attr_value")
        """
        match = re.match(r"^(\w+)\.(\w+)\((.*)\)$", line)
        if not match:
            return super().default(line)

        cls_name, command, args = match.groups()

        if cls_name not in self.dict_of_classes:
            print("** class doesn't exist **")
            return

        if command == "all":
            return self.do_all(cls_name)

        elif command == "count":
            return self.count(cls_name)

        elif command == "show":
            obj_id = args.strip().strip('"').strip("'")
            return self.do_show(f"{cls_name} {obj_id}")

        elif command == "destroy":
            obj_id = args.strip().strip('"').strip("'")
            return self.do_destroy(f"{cls_name} {obj_id}")

        elif command == "update":
            tokens = args.split(",", 2)
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            obj_id = tokens[0].strip().strip('"').strip("'")

            if len(tokens) < 3:
                print("** attribute name missing **")
                return

            attr_name = tokens[1].strip().strip('"').strip("'")
            try:
                attr_value = tokens[2].strip()
            except IndexError:
                print("** value missing **")
                return

            return self.do_update(f'{cls_name} {obj_id} {attr_name} {attr_value}')

        else:
            return super().default(line)
            



    def count(self, cls_name):
        """
        Count instances of a specific class.
        
        This method counts the number of instances of a given class name
        currently stored in the storage system and prints the count.
        
        Args:
            cls_name (str): Name of the class to count instances for.
            
        Returns:
            None: Prints the count to stdout.
            
        Example:
            >>> cmd = HBNBCommand()
            >>> cmd.count("User")
            3
            >>> cmd.count("BaseModel") 
            7
            
        Note:
            This method is typically called via dot notation: ClassName.count()
        """
        res = 0
        all_objects = storage.all()
        for i in all_objects:
            if all_objects[i].__class__.__name__ == cls_name:
                res += 1
        print(res)



    def do_create(self, line):
        """
        Create a new instance of a specified class.
        
        This method creates a new instance of the specified class, saves it
        to the storage system, and prints the unique ID of the created instance.
        
        Args:
            line (str): Command line containing the class name.
            
        Returns:
            None: Prints the new instance ID or error messages.
            
        Raises:
            No explicit exceptions, but prints error messages for:
            - Missing class name
            - Non-existent class name
            
        Example:
            (hbnb) create User
            f47ac10b-58cc-4372-a567-0e02b2c3d479
            (hbnb) create BaseModel
            6cfb47c4-a434-4da7-ac03-2122624c3762
            (hbnb) create InvalidClass
            ** class doesn't exist **
        """
        args = line.split()
        try:
            cls_name = args[0]
        except IndexError:
            print("** class name missing **")
            return
        if cls_name in self.dict_of_classes:
            temp = self.dict_of_classes[cls_name]()
            temp.save()
            print(temp.id)
        else:
            print("** class doesn't exist **")


    def do_show(self, line):
        """
        Display the string representation of an instance.
        
        This method retrieves and displays the string representation of an
        instance based on the class name and instance ID.
        
        Args:
            line (str): Command line containing class name and instance ID.
                       Format: "ClassName instance_id"
            
        Returns:
            None: Prints the instance representation or error messages.
            
        Raises:
            No explicit exceptions, but prints error messages for:
            - Missing class name
            - Non-existent class
            - Missing instance ID
            - Instance not found
            
        Example:
            (hbnb) show User 1234-1234-1234
            [User] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': ...}
            (hbnb) show User
            ** instance id missing **
            (hbnb) show InvalidClass 1234
            ** class doesn't exist **
        """
        args = line.split()
        try:
            cls_name = args[0]
        except IndexError:
            print("** class name missing **")
            return
        if cls_name not in self.dict_of_classes:
            print("** class doesn't exist **")
            return
        try:
            id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        obj_id = "{}.{}".format(cls_name, id)
        all_objects = storage.all()
        if obj_id in all_objects:
            print(all_objects[obj_id])
        else:
            print("** no instance found **")


    def do_destroy(self, line):
        """
        Delete an instance based on class name and ID.
        
        This method deletes an instance from the storage system based on
        the provided class name and instance ID, then saves the changes.
        
        Args:
            line (str): Command line containing class name and instance ID.
                       Format: "ClassName instance_id"
            
        Returns:
            None: Prints error messages if deletion fails.
            
        Raises:
            No explicit exceptions, but prints error messages for:
            - Missing class name
            - Non-existent class
            - Missing instance ID
            - Instance not found
            
        Example:
            (hbnb) destroy User 1234-1234-1234
            (hbnb) destroy User 1234-1234-1234
            ** no instance found **
            (hbnb) destroy User
            ** instance id missing **
            
        Note:
            Successfully deleted instances produce no output.
        """
        args = line.split()
        try:
            cls_name = args[0]
        except IndexError:
            print("** class name missing **")
            return
        if cls_name not in self.dict_of_classes:
            print("** class doesn't exist **")
            return
        try:
            id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        obj_id = "{}.{}".format(cls_name, id)
        all_objects = storage.all()
        if obj_id in all_objects:
            del all_objects[obj_id]
            storage.save()
        else:
            print("** no instance found **")



    def do_all(self, line):
        """
        Display string representations of all instances or instances of a specific class.
        
        This method retrieves and displays string representations of instances.
        If no class name is provided, it shows all instances. If a class name
        is provided, it shows only instances of that class.
        
        Args:
            line (str): Optional class name to filter instances.
                       If empty, shows all instances.
            
        Returns:
            None: Prints a list of instance representations.
            
        Raises:
            No explicit exceptions, but prints error messages for:
            - Non-existent class name
            
        Example:
            (hbnb) all
            ["[User] (1234) {...}", "[BaseModel] (5678) {...}"]
            (hbnb) all User
            ["[User] (1234) {...}", "[User] (9876) {...}"]
            (hbnb) all InvalidClass
            ** class doesn't exist **
            (hbnb) all State
            []
            
        Note:
            Output is formatted as a list of dictionary string representations.
            Returns "[]" if no matching instances are found.
        """
        look_for = '.'
        if line:
            if line in self.dict_of_classes:
                look_for = line
            else:
                print("** class doesn't exist **")
                return
        all_objects = storage.all()
        str_all = "["
        spark = 1
        for i in all_objects:
            spark = 0
            if look_for in i:
                str_all += "\"" + str(all_objects[i].to_dict()) + "\", "
        if spark:
            str_all = "[]"
        else:
            str_all = str_all[:-2] + "]"
        print(str_all)



    def do_update(self, line):
        """
        Update an instance attribute based on class name and ID.
        
        This method updates a single attribute of an existing instance.
        It handles type conversion for integer and float values and prevents
        modification of protected attributes (id, created_at, updated_at).
        
        Args:
            line (str): Command line with class name, ID, attribute name, and value.
                       Format: "ClassName instance_id attribute_name attribute_value"
            
        Returns:
            None: Updates the instance and saves changes, or prints error messages.
            
        Raises:
            No explicit exceptions, but prints error messages for:
            - Missing class name
            - Non-existent class
            - Missing instance ID
            - Instance not found
            - Missing attribute name
            - Missing attribute value
            
        Example:
            (hbnb) update User 1234-1234-1234 email "test@example.com"
            (hbnb) update User 1234-1234-1234 age 25
            (hbnb) update User 1234-1234-1234 height 5.9
            (hbnb) update User 1234-1234-1234 id "new-id"  # Ignored
            (hbnb) update User
            ** instance id missing **
            
        Note:
            - String values can be quoted to preserve spaces
            - Numeric values are automatically converted to int/float
            - Protected attributes (id, created_at, updated_at) are ignored
            - Only processes the first 4 arguments to prevent accidental updates
        """
        args = shlex.split(line)
        try:
            cls_name = args[0]
        except IndexError:
            print("** class name missing **")
            return
        if cls_name not in self.dict_of_classes:
            print("** class doesn't exist **")
            return
        try:
            id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        obj_id = "{}.{}".format(cls_name, id)
        all_odjs = storage.all()
        if obj_id not in all_odjs:
            print("** no instance found **")
            return 
        try:
            attr_name = args[2]
        except IndexError:
            print("** attribute name missing **")
            return
        try:
            value = args[3]
        except IndexError:
            print("** value missing **")
            return
        if attr_name == "id" or attr_name == "created_at" or attr_name == "updated_at":
            return
        if len(args) > 4:
            return
        
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass

        setattr(all_odjs[obj_id], attr_name, value)
        all_odjs[obj_id].save()


        setattr(all_odjs[obj_id], attr_name, value)
        all_odjs[obj_id].save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()

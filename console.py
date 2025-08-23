#!/usr/bin/python3
"""
Entry point of the command interpreter for the HBNB project.
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


from models import storage

import shlex
import cmd

class HBNBCommand(cmd.Cmd):

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
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

#---------------------------------------------------------
    def do_create(self, line):
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

#---------------------------------------------------------
    def do_show(self, line):
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


#---------------------------------------------------------
    def do_destroy(self, line):
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


#---------------------------------------------------------
    def do_all(self, line):
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



#---------------------------------------------------------
    #update <class name> <id> <attribute name> "<attribute value>"
    def do_update(self, line):
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

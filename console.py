#!/usr/bin/python3
"""
Entry point of the command interpreter for the HBNB project.
"""
from models.base_model import BaseModel
from models import storage

import cmd

class HBNBCommand(cmd.Cmd):

    set_of_classes = {
        "BaseModel"
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
        if cls_name == "BaseModel":
            temp = BaseModel()
            print(temp.id)
            temp.save()
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
        if cls_name not in self.set_of_classes:
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
        if cls_name not in self.set_of_classes:
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
        else:
            print("** no instance found **")


#---------------------------------------------------------
    def do_all(self, line):
        look_for = '.'
        if line:
            if line in self.set_of_classes:
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




if __name__ == '__main__':
    HBNBCommand().cmdloop()

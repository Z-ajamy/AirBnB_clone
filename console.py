#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command interpreter for the HBNB project"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Handle EOF (Ctrl+D) to exit"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

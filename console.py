#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_quit(self, line):
        return True
    def do_EOF(self, line):
        return True
    def do_help(self, line):
        print("\nDocumented commands (type help <topic>):" \
        "\n========================================\n" \
        "EOF  help  quit\n")
if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
"""documentation needed here"""

class HBNBCommand(cmd.Cmd):
    """the prompt message to recursively display"""
    prompt = "(hbnd) "

    global clas
    clas = ["BaseModel"]

    def do_quit(self, arg):
        """Quit (hbnd) CLI\n"""
        return True

    def do_EOF(self, arg):
        """Quit (hbnd) CLI\n"""
        return True

    def emptyline(self):
        """An emptyline leave the CLI with no action\n"""
        pass

    def do_create(self, arg):
        """Create an instance of the BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in clas:
            print("** class doesn't exist **")
        else:
            new_inst = BaseModel()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        """Display the string representation of an instance base on
        class name and id"""
        lst = arg.split()
        if arg and lst[0] in clas:
            cl_name = lst[0] + "()"
            print(cl_name)
        if not arg:
            print("** class name missing **")
        elif lst[0] not in clas:
            print("** class doesn't exist **")
        elif len(lst) < 2:
            print("** instance id missing **")
        elif lst[1] != cl_name.id:
            print("** no instance found **")
        else:
            print("pass") #Currently working on this


if __name__ == '__main__':
    HBNBCommand().cmdloop()

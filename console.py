#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import re

class HBNBCommand(cmd.Cmd):
    clas = {'BaseModel': BaseModel}
    prompt = "(hbnd) "

    def do_quit(self, arg):
        '''Quit (hbnd) CLI\n'''
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
        elif arg not in self.clas.keys():
            print("** class doesn't exist **")
        else:
            new_inst = self.clas[arg]()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        """Display the string representation of an instance base on
        class name and id"""
        lst = arg.split()

        if not arg:
            print("** class name missing **")
            return
        elif lst[0] not in self.clas.keys():
            print("** class doesn't exist **")
            return
        elif len(lst) < 2:
            print("** instance id missing **")
            return

        obj_all = storage.all()

        key = "{}.{}".format(lst[0], lst[1])
        if key not in obj_all:
            print("** no instance found **")
            return

        print(obj_all[key])

    def do_destroy(self, arg):
        """Delete an instance considering the class name and its id"""
        lst = arg.split()

        if not arg:
            print("** class name missing **")
            return
        elif lst[0] not in self.clas.keys():
            print("** class doesn't exist **")
            return
        elif len(lst) < 2:
            print("** instance id missing **")
            return

        all_obj = storage.all()
        key = "{}.{}".format(lst[0], lst[1])
        if key not in all_obj:
            print("** no instance found **")
            return

        del all_obj[key]
        storage.save()

    def do_all(self, arg):
        """Display all the instances in the dictionary"""
        lst = arg.split()
        if not arg:
            obj = storage.all()
            for key, value in obj.items():
                new = obj[key]
                #format_new = json.loads(str(new))
                print(new)
                #print(format_new)
            return

        '''The all method works fine but the issue of making it a list and
        string type remains the case now, I have tried to implement it without
        hard coding, pleae look into it if you can implement the code to work
        as required. this is almost 5am, let me sleep for 2hours. Good morning'''

        if arg not in self.clas.keys():
            print("** class doesn't exist **")
        elif arg in self.clas.keys():
            obj = storage.all()
            #new_dict_class = {}
            for key, value in obj.items():
                keys, values = key.split(".")
            use_clas = keys
            if keys in self.clas.keys():
                if key.startswith(use_clas):
                    for key, val in obj.items():
                        chimeMyGuy = obj[key]
                        print(chimeMyGuy)

    def do_update(self, arg):
        """Update the class object by adding new attributes"""
        #pattern = r'\s+(?=([^"]*"[^"]*")*[^"]*$)'
        #lst = re.split(pattern, arg)
        lst = arg.split()
        all_storage = storage.all()
        #chk_key = "{}.{}".format(lst[0], lst[1])
        #key, value = all_storage.split(".")

        if not arg:
            print("** class name missing **")
        elif lst[0] not in self.clas.keys():
            print("** class doesn't exist **")
        elif len(lst) < 2:
            print("** instance id missing **")
        elif lst[1]:
            chk_key = "{}.{}".format(lst[0], lst[1])
            if chk_key not in all_storage:
                print("** no instance found **")
            elif len(lst) < 3:
                print("** attribute name missing **")
            elif len(lst) < 4:
                print("** value missing **")
            else:
                key = str(lst[2])
                new_dict = {}
                new_dict = all_storage[chk_key]
                setattr(new_dict, key, lst[3].strip('"'))
                #new_dict[key] = {lst[3]}
                #new_dict.append({str(lst[2]): lst[3]})
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

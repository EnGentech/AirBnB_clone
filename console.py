#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    clas = {'BaseModel': BaseModel, 'City': City, 'Amenity': Amenity,
            'User': User, 'State': State, 'Place': Place, 'Review': Review}
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
        """Display all the instances in the dictionary\n"""
        split_args = arg.split()
        # splits arg received
        objects = storage.all()
        # store a copy of FileStorage dictionary
        hold_string_to_print = []
        # empty list to hold what to print

        if len(split_args) == 0:
            # if no argument is passed to all
            for value in objects.values():
                # loop through all values in objects
                hold_string_to_print.append(str(value))
                # convert every value in object to string and
                # add every value in object to the list of arguments to print
                # this means that hold_string_to_print stores
                # all values of objects
        elif split_args[0] in self.clas.keys():
            # if first argument is defined as a key in clas (i.e) dictionary
            for key, value in objects.items():
                # loop through each key and value in object items
                if split_args[0] in key:
                    # if first arg matches any key in object items
                    hold_string_to_print.append(str(value))
                    # add the value of that key to our list we want to print
        else:
            print("** class doesn't exist **")

        print(hold_string_to_print)

    def do_update(self, arg):
        """Update the class object by adding new attributes"""
        # pattern = r'\s+(?=([^"]*"[^"]*")*[^"]*$)'
        # lst = re.split(pattern, arg)
        lst = arg.split()
        all_storage = storage.all()
        # chk_key = "{}.{}".format(lst[0], lst[1])
        # key, value = all_storage.split(".")

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
                # new_dict[key] = {lst[3]}
                # new_dict.append({str(lst[2]): lst[3]})
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

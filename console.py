#!/usr/bin/env python3
# console.py
"""entry point of the command interpreter"""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models import storage


# dict of classes
classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "Place": Place, "City": City, "Review": Review, "State": State}

# function to parse arguments


def parse(arg):
    """Convert a args string into an argument list"""
    return shlex.split(arg)

# checks arguments


def arg_check(arg):
    """Checks the argument and returns the correct error messages or key"""
    if arg:
        args = parse(arg)
    else:
        print("** class name missing **")
        return None
    if args[0]:
        if len(args) > 1:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                key = f"{args[0]}.{args[1]}"
                return key
        else:
            print("** instance id missing **")
    else:
        print("** class name missing **")


class HBNBCommand(cmd.Cmd):
    """class definition for the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Method when an empty line is entered in response to the prompt."""
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel Ex: $ create BaseModel
        """
        if arg:
            if arg not in classes:
                print("** class doesn't exist **")
            else:
                new_model = classes[arg]()
                new_model.save()
                print(new_model.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance based\
            on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234
        """
        key = arg_check(arg)
        if key is not None:
            if key in storage.all():
                print(storage.all().get(key))
            else:
                print("** no instance found **")
        else:
            return False

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        key = arg_check(arg)
        if key is not None:
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print("** no instance found **")
        else:
            return False

    def do_all(self, arg):
        """
        Prints all string representation of all instances\
         based or not on the class name
        """
        str_list = []
        for k, v in storage.all().items():
            if arg:
                if arg not in classes:
                    print("** class doesn't exist")
                    return False
                if arg == v.__class__.__name__:
                    str_list.append(str(v))
            else:
                str_list.append(str(v))
        print(str_list)

    def do_update(self, arg):
        """updates an instance based on the classname and id\
        by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if arg:
            args = parse(arg)
        else:
            print("** class name missing **")
            return None
        if args[0]:
            if len(args) > 1:
                if args[0] not in classes:
                    print("** class doesn't exist **")
                else:
                    key = f"{args[0]}.{args[1]}"
                    if key in storage.all():
                        if args[2]:
                            if args[3]:
                                setattr(storage.all()[key], args[2], args[3])
                                storage.all().get(key).save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
        If this method is not overridden, it prints an error message and
        returns.
        """
        args = line.split('.')
        if args[0] in classes:

            if args[1] == "all()":
                for k, v in storage.all().items():
                    if v.__class__.__name__ == args[0]:
                        print(v)

            elif args[1] == "count()":
                count = 0
                for k, v in storage.all().items():
                    if v.__class__.__name__ == args[0]:
                        count += 1
                print(count)

            elif args[1].startswith("show"):
                id = args[1].rstrip("show()\"")
                key = args[0] + "." + id
                if key in storage.all():
                    print(storage.all().get(key))
                else:
                    print("No instance found")

            elif args[1].startswith("destroy"):
                id_r = args[1][8:][:-2]
                id = id_r.strip("\"")
                key = args[0] + "." + id
                print(key)
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("No instance found")

            else:
                print("** Invalid command **")
        else:
            self.stdout.write('*** Unknown syntax: %s\n' % line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

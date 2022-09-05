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


def parse(arg):
    """Convert a args string into an argument list"""
    return shlex.split(arg)


def arg_check(arg):
    """Checks the argument and returns the correct error messages or key"""
    if arg:
        args = parse(arg)
    else:
        print("** class name missing **")
        return None
    if args[0]:
        if args[0] not in classes:
            print("** class doesn't exist **")
        else:
            if len(args) > 1:
                key = f"{args[0]}.{args[1]}"
                return key
            else:
                print("** instance id missing **")
    else:
        print("** class name missing **")


class HBNBCommand(cmd.Cmd):
    """class definition for the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of file command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Method when an empty line is entered in response to the prompt."""
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel Ex: $ create BaseModel
        """
        if arg:
            args = parse(arg)
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                new_model = classes[args[0]]()
                new_model.save()
                print(new_model.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance based
            on the class name and id.
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
        Prints all string representation of all instances
        based or not on the class name
        """
        str_list = []
        if arg:
            if arg not in classes:
                print("** class doesn't exist **")
                return False
            for k, v in storage.all().items():
                if arg == v.__class__.__name__:
                    str_list.append(str(v))
        else:
            for k, v in storage.all().items():
                str_list.append(str(v))
        print(str_list)

    def do_update(self, arg):
        """updates an instance based on the classname and id"""
        if arg:
            args = parse(arg)
        else:
            print("** class name missing **")
            return None
        if args[0]:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                if len(args) > 1:
                    key = f"{args[0]}.{args[1]}"
                    if key in storage.all():
                        if args[2]:
                            if args[3]:
                                setattr(storage.all()[
                                        key], args[2], args[3])
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
        new_list = []
        args = line.split('.')
        if args[0] in classes:

            if args[1] == "all()":
                for k, v in storage.all().items():
                    if v.__class__.__name__ == args[0]:
                        new_list.append(v)
                print(new_list)

            elif args[1] == "count()":
                count = 0
                for k, v in storage.all().items():
                    if v.__class__.__name__ == args[0]:
                        count += 1
                print(count)

            elif args[1].startswith("show"):
                id_r = args[1][5:][:-1]
                id = id_r.strip("\"")
                key = args[0] + "." + id
                if key in storage.all():
                    print(storage.all().get(key))
                else:
                    print("** no instance found **")

            elif args[1].startswith("destroy"):
                id_r = args[1][8:][:-1]
                id = id_r.strip("\"")
                if len(id) < 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + id
                    if key in storage.all():
                        storage.all().pop(key)
                        storage.save()
                    else:
                        print("** no instance found **")

            elif args[1].startswith("update"):
                attributes = args[1][7:-1]
                attr_list = [i.rstrip(",\"").lstrip(",\"")
                             for i in attributes.split()]
                if attr_list[0]:
                    key = args[0] + "." + attr_list[0]
                    if key in storage.all():
                        if attr_list[1]:
                            if attr_list[2]:
                                setattr(storage.all()[
                                        key], attr_list[1], attr_list[2])
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
                print("** Invalid command **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

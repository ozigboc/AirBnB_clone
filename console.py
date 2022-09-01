#!/usr/bin/python3
# console.py
"""entry point of the command interpreter"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage


classes = ["BaseModel", "User"]


class HBNBCommand(cmd.Cmd):
    """class definition for the command interpreter"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel Ex: $ create BaseModel"""
        if arg:
            if arg != "BaseModel":
                print("** class doesn't exist **")
            else:
                new_model = BaseModel()
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
            storage.all().pop(key)
            storage.save()
        else:
            return False

    def do_all(self, arg):
        """
        Prints all string representation of all instances\
         based or not on the class name
        """
        str_list = []
        if arg:
            if arg not in classes:
                print("** class doesn't exist")
                return False
        for k, v in storage.all().items():
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

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Method when an empty line is entered in response to the prompt."""
        pass


def parse(arg):
    'Convert a args string into an argument list'
    return shlex.split(arg)


def arg_check(arg):
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

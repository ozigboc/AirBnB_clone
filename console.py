#!/usr/bin/python3
# console.py
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel

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
                pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()


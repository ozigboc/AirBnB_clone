#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import pep8
import sys
from io import StringIO
import re
import os
console = HBNBCommand()


class TestHBNBCommand(unittest.TestCase):

    """Tests HBNBCommand console."""

    attribute_values = {
        str: "foobar108",
        int: 1008,
        float: 1.08
    }

    reset_values = {
        str: "",
        int: 0,
        float: 0.0
    }

    test_random_attributes = {
        "strfoo": "barfoo",
        "intfoo": 248,
        "floatfoo": 9.8
    }

    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update\n
"""
        self.assertEqual(s, f.getvalue())

    def test_do_quit(self):
        """Tests quit commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    def test_do_EOF(self):
        """Tests EOF commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

    def test_emptyline(self):
        """Tests emptyline functionality."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        s = ""
        self.assertEqual(s, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
        s = ""
        self.assertEqual(s, f.getvalue())

    def test_do_create(self):
        """Tests create for all classes."""
        for classname in self.classes():
            self.help_test_do_create(classname)

    def help_test_do_create(self, classname):
        """Helper method to test the create commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        key = "{}.{}".format(classname, uid)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(classname))
        self.assertTrue(uid in f.getvalue())

    def test_do_create_error(self):
        """Tests create command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create garbage")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def help_test_do_show(self, classname):
        """Helps test the show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show {} {}".format(classname, uid))
        s = f.getvalue()[:-1]
        self.assertTrue(uid in s)

    def test_do_show_error(self):
        """Tests show command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show garbage")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 6524359")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

    def help_test_show_advanced(self, classname):
        """Helps test .show() command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertTrue(uid in s)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage.show()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show("6524359")')
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

    def test_do_destroy(self):
        """Tests destroy for all classes."""
        for classname in self.classes():
            self.help_test_do_destroy(classname)
            self.help_test_destroy_advanced(classname)

    def help_test_do_destroy(self, classname):
        """Helps test the destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy {} {}".format(classname, uid))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(uid in f.getvalue())

    def test_do_destroy_error(self):
        """Tests destroy command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy garbage")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 6524359")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

    def help_test_destroy_advanced(self, classname):
        """Helps test the destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.destroy("{}")'.format(classname, uid))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(uid in f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage.destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.destroy("6524359")')
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

    def test_do_all(self):
        """Tests all for all classes."""
        for classname in self.classes():
            self.help_test_do_all(classname)
            self.help_test_all_advanced(classname)

    def help_test_do_all(self, classname):
        """Helps test the all command."""
        uid = self.create_class(classname)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertIn(uid, s)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(classname))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertIn(uid, s)

    def test_do_all_error(self):
        """Tests all command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all garbage")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def help_test_all_advanced(self, classname):
        """Helps test the .all() command."""
        uid = self.create_class(classname)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.all()".format(classname))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)

    def test_do_all_error_advanced(self):
        """Tests all() command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage.all()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def test_count_all(self):
        """Tests count for all classes."""
        for classname in self.classes():
            self.help_test_count_advanced(classname)

    def help_test_count_advanced(self, classname):
        """Helps test .count() command."""
        for i in range(20):
            uid = self.create_class(classname)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.count()".format(classname))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertEqual(s, "20")

    def test_do_count_error(self):
        """Tests .count() command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage.count()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def test_update_error(self):
        """Test alternate update command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("sldkfjsl.update()")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(12345)")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(" + id + ")")
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(" + id + ", name)")
            self.assertEqual(
                "** value missing **\n", f.getvalue())

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
                     {"place_id": str,
                      "user_id": str,
                      "text": str}
        }
        return attributes

    def create_class(self, classname):
        """Creates a class for console tests."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        return uid

    def help_load_dict(self, rep):
        """Helper method to test dictionary equality."""
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(rep)
        self.assertIsNotNone(res)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        return d


class TestConsoleDocs(unittest.TestCase):
    """testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8 rules."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand console."""

    def setUp(self):
        """Set up a clean storage for each test."""
        storage._FileStorage__objects = {}

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_eof(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        """Test no action on an empty line."""
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd(""))

    def test_create_missing_class(self):
        """Test create with no class name."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("create")
            self.assertEqual(out.getvalue().strip(),
                             "** class name missing **")

    def test_create_invalid_class(self):
        """Test create with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(out.getvalue().strip(),
                             "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test create with a valid class name."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("create BaseModel")
            instance_id = out.getvalue().strip()
            key = f"BaseModel.{instance_id}"
            self.assertIn(key, storage.all())

    def test_show_missing_class(self):
        """Test show with no class name."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("show")
            self.assertEqual(out.getvalue().strip(),
                             "** class name missing **")

    def test_show_invalid_class(self):
        """Test show with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(out.getvalue().strip(),
                             "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show with no instance id."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(out.getvalue().strip(),
                             "** instance id missing **")

    def test_show_invalid_id(self):
        """Test show with an invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("show BaseModel 1234")
            self.assertEqual(out.getvalue().strip(), "** no instance found **")

    def test_show_valid(self):
        """Test show with a valid class name and id."""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd(f"show BaseModel {obj.id}")
            self.assertIn(str(obj), out.getvalue().strip())

    def test_destroy_missing_class(self):
        """Test destroy with no class name."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(out.getvalue().strip(),
                             "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(out.getvalue().strip(),
                             "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy with no instance id."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(out.getvalue().strip(),
                             "** instance id missing **")

    def test_destroy_invalid_id(self):
        """Test destroy with an invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("destroy BaseModel 1234")
            self.assertEqual(out.getvalue().strip(), "** no instance found **")

    def test_destroy_valid(self):
        """Test destroy with a valid class name and id."""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd(f"destroy BaseModel {obj.id}")
            self.assertNotIn(f"BaseModel.{obj.id}", storage.all())

    def test_all_no_args(self):
        """Test all with no arguments."""
        obj1 = BaseModel()
        obj2 = User()
        obj1.save()
        obj2.save()
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("all")
            output = out.getvalue().strip()
            self.assertIn(str(obj1), output)
            self.assertIn(str(obj2), output)

    def test_all_valid_class(self):
        """Test all with a valid class name."""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("all BaseModel")
            output = out.getvalue().strip()
            self.assertIn(str(obj), output)

    def test_all_invalid_class(self):
        """Test all with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(out.getvalue().strip(),
                             "** class doesn't exist **")

    def test_update_missing_class(self):
        """Test update with no class name."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("update")
            self.assertEqual(out.getvalue().strip(),
                             "** class name missing **")

    def test_update_invalid_class(self):
        """Test update with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(out.getvalue().strip(),
                             "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update with no instance id."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(out.getvalue().strip(),
                             "** instance id missing **")

    def test_update_invalid_id(self):
        """Test update with an invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("update BaseModel 1234")
            self.assertEqual(out.getvalue().strip(), "** no instance found **")

    def test_update_missing_attribute(self):
        """Test update with no attribute name."""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd(f"update BaseModel {obj.id}")
            self.assertEqual(out.getvalue().strip(),
                             "** attribute name missing **")

    def test_update_missing_value(self):
        """Test update with no attribute value."""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd(f"update BaseModel {obj.id} name")
            self.assertEqual(out.getvalue().strip(), "** value missing **")

    def test_update_valid(self):
        """Test update with valid data."""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd(f'update BaseModel {obj.id} name "John"')
            self.assertEqual(obj.name, "John")


if __name__ == "__main__":
    unittest.main()

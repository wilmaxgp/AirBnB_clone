import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'test'")
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertIn("name", f.getvalue())
            self.assertIn("test", f.getvalue())

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("count BaseModel")
            self.assertIn("2", f.getvalue())

    def test_update_with_dictionary(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(
                f"update BaseModel {obj_id} {{'name': 'test'}}"
            )
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertIn("name", f.getvalue())
            self.assertIn("test", f.getvalue())

    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            self.assertIn("** Unknown command **", f.getvalue())


if __name__ == "__main__":
    unittest.main()

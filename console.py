#!/usr/bin/env python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    intro = 'A CLI for AirBnB Clone ALX Group Project'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print()
        return True

    def do_help(self, arg):
        """List available commands with 'help'."""
        if arg:
            super().do_help(arg)
        else:
            print("\nDocumented commands (type help <topic>):\n")
            print("=" * 40)
            print("EOF  help  quit\n")

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string of an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        if class_name not in
        ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        obj_key = class_name + "." + obj_id
        if obj_key in storage.all():
            print(storage.all()[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
                    (save the change into the JSON file)."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        if class_name not in
        ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        obj_key = class_name + "." + obj_id
        if obj_key in storage.all():
            del storage.all()[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of
            all instances based on the class name."""
        args = arg.split()
        class_name = args[0] if args else None
        if class_name not in
        ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        print(
            [str(obj) for obj in storage.all().values()
                if isinstance(obj, eval(class_name))]
            )

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]
        if class_name not in
        ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        obj_key = class_name + "." + obj_id
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        setattr(storage.all()[obj_key], attribute_name, attribute_value)
        storage.save()

    def do_count(self, arg):
        """Counts the number of instances of a class."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in
        ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        print(
            len(
                [obj for obj in storage.all().values()
                    if isinstance(obj, eval(args[0]))]
            )
        )


if __name__ == '__main__'
HBNBCommand().cmdloop()

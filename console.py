#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    intro = 'A Command Line Interpreter (CLI) for AirBnB Clone ALX Group Project'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print()
        return True

    def do_help(self, arg):
        """List available commands with "help" or detailed help with "help cmd"."""
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
        """Creates a new instance of BaseModel, saves it (to the JSON file), and prints the id."""
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
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:  # Add other model names here
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        if obj_key in storage.all():
            print(storage.all()[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:  # Add other model names here
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        if obj_key in storage.all():
            del storage.all()[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances based or not on the class name."""
        args = arg.split()
        if args and args[0] not in ["BaseModel"]:  # Add other model names here
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all().values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:  # Add other model names here
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(storage.all()[obj_key], args[2], args[3])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

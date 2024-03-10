#!/usr/bin/env python3
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

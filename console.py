#!/usr/bin/python3
"""
This module defines a command-line interface (CLI) using Python's cmd module.
The `HBNBCommand` class provides basic commands for interacting with instances
of BaseModel and simulating a storage system through JSON serialization.

Commands:
- quit: Exits the program.
- EOF (Ctrl+D): Exits the program.
- create: Creates a new object of a given class.
- show: Displays an object based on class and ID.
- destroy: Deletes an object based on class and ID.
- all: Shows all objects, optionally filtered by class.
- update: Updates an object's attribute based on class, ID, and key-value.

The prompt for the CLI is set to "(hbnb) ".
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command-line interpreter for managing BaseModel objects."""

    allowed_classes = ['BaseModel', 'User']
    prompt = "(hbnb) "  # CLI prompt displayed to the user

    def do_quit(self, line):
        """Handles the 'quit' command to exit the program."""
        return True

    def help_quit(self):
        """Displays help text for the 'quit' command."""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """Handles the End of File (Ctrl+D) command to exit."""
        return True

    def emptyline(self):
        """Overrides default behavior; does nothing on empty input."""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a class and saves it to storage.

        Args:
            arg (str): Class name for the instance to be created.

        Usage:
            create <class_name>
        """
        args = arg.split()
        if args:
            if args[0] not in HBNBCommand.allowed_classes:
                print("** class doesn't exist **")
            else:
                obj = eval(f"{args[0]}()")
                print(obj.id)
                obj.save()
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Shows the string representation of an instance by class name and ID.

        Args:
            arg (str): Class name and ID.

        Usage:
            show <class_name> <id>
        """
        match_attrs = False
        args = arg.split()
        if args:
            if args[0] not in HBNBCommand.allowed_classes:
                print("** class doesn't exist **")
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class name missing **")

        all_objs = storage.all()
        for k, v in all_objs.items():
            attr_names = k.split('.')
            if attr_names[0] == args[0] and attr_names[1] == args[1]:
                match_attrs = True
                obj = eval(f"{args[0]}(**v)")
                print(obj)
                break
        if not match_attrs:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and ID.

        Args:
            arg (str): Class name and ID.

        Usage:
            destroy <class_name> <id>
        """
        match_attrs = False
        args = arg.split()
        if args:
            if args[0] not in HBNBCommand.allowed_classes:
                print("** class doesn't exist **")
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class name missing **")

        all_objs = storage.all()
        for k, v in all_objs.items():
            attr_names = k.split('.')
            if attr_names[0] == args[0] and attr_names[1] == args[1]:
                del all_objs[k]
                storage.save()
                match_attrs = True
                break
        if not match_attrs:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Displays all instances or instances of a specific class.

        Args:
            arg (str): Optional class name to filter instances.

        Usage:
            all [<class_name>]
        """
        list1 = []
        args = arg.split()
        all_objs = storage.all()
        if args:
            if args[0] not in HBNBCommand.allowed_classes:
                print("** class doesn't exist **")
            else:
                for k, v in all_objs.items():
                    obj = eval(f"{args[0]}(**v)")
                    list1.append(obj.__str__())
        else:
            for k, v in all_objs.items():
                class_name = k.split('.')[0]
                obj = eval(f"{class_name}(**v)")
                list1.append(obj.__str__())
        print(list1)

    def do_update(self, arg):
        """
        Updates an instance based on class name, ID, attribute name,
        and value, and saves the change to storage.

        Args:
            arg (str): Class name, ID, attribute, and value.

        Usage:
            update <class_name> <id> <attribute_name> <attribute_value>
        """
        match_id = False
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        else:
            if args[0] not in HBNBCommand.allowed_classes:
                print("** class doesn't exist **")
            else:
                try:
                    args[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        args[2]
                    except IndexError:
                        print("** attribute name missing **")
                    else:
                        try:
                            args[3]
                        except IndexError:
                            print("** value missing **")
                        else:
                            all_objs = storage.all()
                            for k, v in all_objs.items():
                                if k == f"{args[0]}.{args[1]}":
                                    class_name = k.split('.')[0]
                                    obj = eval(f"{class_name}(**v)")
                                    del all_objs[k]
                                    setattr(obj, args[2],
                                            convert_string(args[3]))
                                    obj.save()
                                    match_id = True
                                    break
                            if not match_id:
                                print("** no instance found **")


def convert_string(value):
    """Converts a string to its correct data type."""
    if value.startswith("'") and value.endswith("'") or \
            value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value == "True":
        return True
    elif value == "False":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


if __name__ == "__main__":
    HBNBCommand().cmdloop()  # Start the interactive CLI loop

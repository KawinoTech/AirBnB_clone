#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "  # The prompt displayed in the CLI

    def do_quit(self, line):
        """Handles the 'quit' command."""
        return True  # Returning True exits the command loop

    def help_quit(self):
        """Displays help for the 'quit' command."""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """Handles the EOF (Ctrl+D) signal."""
        return True  # Returning True exits the command loop when EOF is pressed


if __name__ == "__main__":
    HBNBCommand().cmdloop()  # Start the interactive command prompt

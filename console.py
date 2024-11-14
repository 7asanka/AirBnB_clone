#!/use/bin/python3
"""
The console that contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB console
    """
    prompt = "(hbnh) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, artg):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line input"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

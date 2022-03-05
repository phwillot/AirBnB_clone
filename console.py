#!/usr/bin/python3
"""This module contain the terminal of the Hbnb project"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Class that handle the terminal functionality"""

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity",
               "Place", "Review"]

    def do_quit(self, arg):
        """Exits the shell with the command quit"""
        return True

    def do_EOF(self, arg):
        """Ends the shell with CTRL+D (EOF)"""
        print()
        return True

    def emptyline(self):
        """Behavior of the shell when there is emptyline
        as input"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and print the ID"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in self.classes:
            newInstance = eval(arg)()
            storage.save()
            print(newInstance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the clss name and id"""
        arguments = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif arguments[0] in self.classes and len(arguments) == 1:
            print("** instance id missing **")
        else:
            found = False
            all_instances = storage.all()
            for value in all_instances.values():
                if arguments[1] == value.to_dict()['id']:
                    print(value)
                    found = True
                    break
                else:
                    continue
            if found is False:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name id
        (Saving the change into JSON file)"""
        arguments = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif arguments[0] in self.classes and len(arguments) == 1:
            print("** instance id missing **")
        else:
            found = False
            all_instances = storage.all()
            for key, value in all_instances.items():
                if arguments[1] == value.to_dict()['id']:
                    all_instances.pop(key)
                    storage.save()
                    found = True
                    break
                else:
                    continue
            if found is False:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        arguments = arg.split(" ")
        all_instances = storage.all()
        array = []
        if len(arg) == 0:
            for value in all_instances.values():
                array.append(str(value))
            if len(array) > 0:
                print(array)
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for value in all_instances.values():
                if arguments[0] == value.__class__.__name__:
                    array.append(str(value))
            if len(array) > 0:
                print(array)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save change to JSON file)"""
        line = arg.replace(",", "")
        arguments = shlex.split(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif arguments[0] in self.classes and len(arguments) == 1:
            print("** instance id missing **")
        elif arguments[0] in self.classes and len(arguments) >= 2:
            found = False
            all_instances = storage.all()
            for key, value in all_instances.items():
                if arguments[1] == value.to_dict()['id']:
                    found = True
                    if len(arguments) == 2:
                        print("** attribute name missing **")
                    if len(arguments) == 3:
                        print("** value missing **")
                    if len(arguments) >= 4:
                        strLine = f"{arguments[0]}.{arguments[1]}"
                        setattr(all_instances[strLine],
                                arguments[2], arguments[3])
                        storage.save()
                    break
                else:
                    continue
            if found is False:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

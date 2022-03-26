# AirBnB_clone

## Description of the project:

In this series of projects I'll build a simplified "clone" of the AirBnB website, the first step presented here is to build a command interpreter to manage AirBnB objects.

List of the class used:

- **BaseModel:** take care of the initialization, serialization and deserialization of the instances.

- **FileStorage:** as its name says, it'll be the storage engine of the project. Saving the instances into JSON format, and reloading all the JSON instances into Python Object.

- (**User, State, City, Place, Amenity):** all theses classes inherits from BaseModel, it'll represent all the objects needed for the website.

## Description of the command intepreter:

### How to start the command interpreter ?
After you cloned the repo, you have to stay at the root of the project and use this command:
```sh
./console.py
```

A prompt ```(hbnb)``` will appear waiting for commands.

### How to use it ?
You can use the ```help``` command to see all the commands available and type ```help <command>``` for more details on it.

## Examples
List of commands available: 
- **quit:** Exits the shell.
- **EOF:** Exist the shell when typing CTRL + D.
- **help:** Help on any command available.
- **create:** Creates a new instance of any classes available.
- **show:** Prints the string representation of an instance.
- **destroy:** Deletes an instance based on the class name and id.
- **all:** Prints all string representation of all instances based or not on the class name.
- **update:** Updates an instanced based on the class name and id by adding or updating attributes.

### **create example**
The command below will create an instance of BaseModel class, save it to the JSON file, and print the id.
```sh
(hbnb) create BaseModel
1234-1234-1234-1234
```

### **show example**
The command below will print the string representation of the BaseModel object with the "id" passed to it.
```sh
(hbnb) show BaseModel 1234-1234-1234-1234
[BaseModel] (1234-1234-1234-1234) {'id': '1234-1234-1234-1234', 'created_at': datetime.datetime(2022, 3, 4, 10, 53, 24, 557776), 'updated_at': datetime.datetime(2022, 3, 4, 10, 53, 24, 557776)}
```

### **destroy example**
The command below will destroy the instance with the id passed to it.
```sh
(hbnb) destroy BaseModel 1234-1234-1234-1234
```

### **all example**
The command will print all string representation of the User instances.
```sh
(hbnb) all
["[BaseModel] (634a6a56-21af-40ef-9fc2-9f151e87130d) {'id': '634a6a56-21af-40ef-9fc2-9f151e87130d', 'created_at': datetime.datetime(2022, 3, 4, 9, 56, 31, 832488), 'updated_at': datetime.datetime(2022, 3, 4, 9, 56, 31, 832488)}", "[User] (ec4b2d1c-175f-475d-8c14-9e22fa1c0a5e) {'id': 'ec4b2d1c-175f-475d-8c14-9e22fa1c0a5e', 'created_at': datetime.datetime(2022, 3, 4, 9, 56, 57, 787836), 'updated_at': datetime.datetime(2022, 3, 4, 9, 56, 57, 787836)}", "[BaseModel] (e9f709da-60dd-489c-8142-45ffdbfde109) {'id': 'e9f709da-60dd-489c-8142-45ffdbfde109', 'created_at': datetime.datetime(2022, 3, 4, 10, 53, 24, 557776), 'updated_at': datetime.datetime(2022, 3, 4, 10, 53, 24, 557776)}", "[User] (3f4c79f6-d40e-4d4c-936e-c224412137e6) {'id': '3f4c79f6-d40e-4d4c-936e-c224412137e6', 'created_at': datetime.datetime(2022, 3, 4, 10, 58, 11, 599140), 'updated_at': datetime.datetime(2022, 3, 4, 10, 58, 11, 599140)}"]
(hbnb) all User
["[User] (ec4b2d1c-175f-475d-8c14-9e22fa1c0a5e) {'id': 'ec4b2d1c-175f-475d-8c14-9e22fa1c0a5e', 'created_at': datetime.datetime(2022, 3, 4, 9, 56, 57, 787836), 'updated_at': datetime.datetime(2022, 3, 4, 9, 56, 57, 787836)}", "[User] (3f4c79f6-d40e-4d4c-936e-c224412137e6) {'id': '3f4c79f6-d40e-4d4c-936e-c224412137e6', 'created_at': datetime.datetime(2022, 3, 4, 10, 58, 11, 599140), 'updated_at': datetime.datetime(2022, 3, 4, 10, 58, 11, 599140)}"]
```
### **update example**
This command will update the attribute name of the instance User with the id passed to it.
```sh
update User 3f4c79f6-d40e-4d4c-936e-c224412137e6 name "Georges"
```

## web_static

In this folder, you can find the HTML and the CSS used for the static representation of the web page.

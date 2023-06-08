<p align="center">
# AirBnB Clone - The Console
</p>

![HaBnB](https://github.com/Nomad-Rob/holbertonschool-AirBnB_clone/assets/115587964/fff9dd61-8a10-4f07-8d06-cefec834806c)

# Description of the project
This is the start of a series of ABnB Projects that will be completed over the next few months. This project is the first step towards building a full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
![Overview of AirBnB](https://github.com/Nomad-Rob/holbertonschool-AirBnB_clone/assets/115587964/f35bc94c-60c7-4318-9f5b-e1baa12ce2b2)

## The console (command interpreter)
The console is a command line interpreter that permits management of the AirBnB objects. With the console you can create a new object, retrieve an object from a file, do operations on objects, update attributes of an object, and destroy an object.

## How to start the console
The console can be started by running the console.py file in an interactive mode:

## How to use the console
The console can be used in two modes: interactive and non-interactive. The non-interactive mode is used when the console is executed in a script mode: echo "help" | ./console.py. The interactive mode is used when the console is executed in an interactive mode: ./console.py and then the user types a command and presses enter, and the console displays the result and prompts for another command, and this continues until the user presses ctrl+c or enters the quit command.

To start and use:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Commands
The console supports the following commands:
Help: displays the documented commands.
Quit: exits the program.
EOF: exits the program.
Create: creates a new instance of a class, saves it (to the JSON file) and prints the id.
Show: prints the string representation of an instance based on the class name and id.
Destroy: deletes an instance based on the class name and id (save the change into the JSON file).
All: prints all string representation of all instances based or not on the class name.
Update: updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

### How to use the commands
The commands can be used in the following format: <command> <class name> <id> <attribute name> "<attribute value>". The command name is always the first word, the class name is always the second word, the id is always the third word, the attribute name is always the fourth word, and the attribute value is always the fifth word. The attribute value must be enclosed in double quotes, and the attribute value must be a string, an integer, or a float. If the attribute value is a string that contains spaces, the entire string must be enclosed in double quotes. If the attribute value is a string that does not contain spaces, the double quotes are optional. If the attribute value is an integer or a float, the double quotes are optional.

### Examples of commands
Create: create <class name>
Show: show <class name> <id>
Destroy: destroy <class name> <id>
All: all <class name>
Update: update <class name> <id> <attribute name> "<attribute value>"
Help: help <command name>
Quit: quit
EOF: EOF

!!!!!!!!!!!!!!!!!!!!SHOW Pictures and examples of commands above!!!!!!!!!

## Classes
The console supports the following classes:

BaseModel: BaseModel class for all other classes.
User: User class.
State: State class.
City: City class.
Amenity: Amenity class.
Place: Place class.
Review: Review class.

!!!!!!!!!!!!!!!!!!SHow all attributes of each class and what they do!!!!!!!!!!!!!!!

!!!!!! Good stopping point for now will need to update at end with pictures and added info. After AT will be able to flowchart this project but from reading and resourcing it seems like it will be a lot of work. !!!!!

!!!!! Still want to practice with pull request on github and code review. Maybe ask someone after AT to practice with !!!!!!

## Authors
> Robert Farley: [Github](https://github.com/Nomad-Rob)

# The AirBnB Clone Project
![AirBnB Logo]
# Project Description
This is the first part of the AirBnB clone project where we
worked on the backend of the project whiles interfacing it
with console application with the help of cmd module in python.

The AirBnB project.

# Description of the command interpreter:
The interface of the application is just like the Bash shell
except has a limited number of accepted commands that were
solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter  serves as the frontend of web app

Some of the commands available are
- show
- create
- update
- destroy
- count

And as part of the implementation of the command line interpreter
coupled with the backend and file storage system, the following
-   Creating new objects(ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Doing operations on objects(count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object

# How to start it
These instructions will get you a copy of the project
up and running on your local machine(Linux distro)
for development and testing purposes.

# Installing

You will need to clone the repository of the project from Github.


git clone https: // github.com/mwahk3ymer/AirBnB_clone.git

After cloning you will have folder called AirBnB_clone.work.

> console.py: The main executable, the command interpreter.
>
> models/engine/file_storage.py: Class serializes instances
to JSON file and deserializes JSON file to instances
>
>models/__ init __.py:  A unique FileStorage instance for app
>
> models/base_model.py: Class that defines all common att/methodss.
>
>models/user.py: User class that inherits from BaseModel
>
>models/state.py: State class that inherits from BaseModel
>
>models/city.py: City class that inherits from BaseModel
>
>models/amenity.py: Amenity class that inherits from BaseModel
>
>models/place.py: Place class that inherits from BaseModel
>
>models/review.py: Review class that inherits from BaseModel

# How to use it
It can work in two different modes
** Interactive ** and ** Non-interactive **

In ** Interactive mode ** the console will display a prompt(hbnb)
indicating that the user can write and execute a command.
After the command is run, the prompt will appear again a wait for
new command.can go indefinitely as long as user does not exit prog


$ echo "help" | ./console.py
(hbnb)

Documented commands
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands
EOF  help  quit
(hbnb)
$


# Format of Command Input

In order to give commands to the console, these will need to
be piped through an echo in case of ** Non-interactive mode **

In ** Interactive Mode ** the commands will need to be written
with a keyboard when the prompt appears and will be recognized
when an enter key is pressed(new line).
As soon as this happens, the console will attempt to execute
command through several means or will show an error message
In this mode, the console can be exited using the ** CTRL + D ** combination
** CTRL + C ** or the command ** quit ** or ** EOF **

# Arguments
In order for the Shell to recognize those parameters, the user must
separate everything with spaces.

Example
user@ubuntu: ~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu: ~/AirBnB$ ./console.py

or

user@ubuntu: ~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu: ~/AirBnB$ ./console.py

# Available commands and what they do

The recognizable commands by the interpreter are the following

| Command | Description |
| **--** | **--** |
| ** quit or EOF ** | Exits the program |
| ** Usage ** | By itself |
| **-----** | **-----** |
| ** help ** | Provides a text describing how to use a command.|
| ** Usage ** | By itself or ** help < command \> ** |
| **-----** | **-----** |
| ** create ** | Create a new instance of a class |

# Author
Audrey Mwakima and Leah Tugi

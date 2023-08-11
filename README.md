# 0x00. AirBnB clone - The console
This project tests comprehension of Python fundamental concepts.
The general task is to build a Python console that contains the entry point of a command interpreter.
The command interpreter implements **quit**, which exits the program, a **Help** action, which provides documentation, and a custom prompt, **hbnb**.

**The command interpreter will implement:**
-   `create`: Creates a new instance of  `BaseModel`, saves it (to the JSON file) and prints the  `id`. Ex:  `$ create BaseModel`
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ create`)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ create MyModel`)
-   `show`: Prints the string representation of an instance based on the class name and  `id`. Ex:  `$ show BaseModel 1234-1234-1234`.
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ show`)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ show MyModel`)
    -   If the  `id`  is missing, print  `** instance id missing **`  (ex:  `$ show BaseModel`)
    -   If the instance of the class name doesn’t exist for the  `id`, print  `** no instance found **`  (ex:  `$ show BaseModel 121212`)
-   `destroy`: Deletes an instance based on the class name and  `id`  (save the change into the JSON file). Ex:  `$ destroy BaseModel 1234-1234-1234`.
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ destroy`)
    -   If the class name doesn’t exist, print  `** class doesn't exist ** (ex:`$ destroy MyModel`)`
    -   If the  `id`  is missing, print  `** instance id missing **`  (ex:  `$ destroy BaseModel`)
    -   If the instance of the class name doesn’t exist for the  `id`, print  `** no instance found **`  (ex:  `$ destroy BaseModel 121212`)
-   `all`: Prints all string representation of all instances based or not on the class name. Ex:  `$ all BaseModel`  or  `$ all`.
    -   The printed result must be a list of strings (like the example below)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ all MyModel`)
-   `update`: Updates an instance based on the class name and  `id`  by adding or updating attribute (save the change into the JSON file). Ex:  `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
    -   Usage:  `update <class name> <id> <attribute name> "<attribute value>"`
    -   Only one attribute can be updated at the time
    -   You can assume the attribute name is valid (exists for this model)
    -   The attribute value must be casted to the attribute type
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ update`)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ update MyModel`)
    -   If the  `id`  is missing, print  `** instance id missing **`  (ex:  `$ update BaseModel`)
    -   If the instance of the class name doesn’t exist for the  `id`, print  `** no instance found **`  (ex:  `$ update BaseModel 121212`)
    -   If the attribute name is missing, print  `** attribute name missing **`  (ex:  `$ update BaseModel existing-id`)
    -   If the value for the attribute name doesn’t exist, print  `** value missing **`  (ex:  `$ update BaseModel existing-id first_name`)
    -   All other arguments should not be used (Ex:  `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"`  =  `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`)
    -   `id`,  `created_at`  and  `updated_at`  cant’ be updated. You can assume they won’t be passed in the  `update`  command
    -   Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime
The project will have a **BaseModel** class that defines all common attributes/methods for other classes as show below:
-   `models/base_model.py`
-   Public instance attributes:
    -   `id`: string - assign with an  `uuid`  when an instance is created:
        -   you can use  `uuid.uuid4()`  to generate unique  `id`  but don’t forget to convert to a string
        -   the goal is to have unique  `id`  for each  `BaseModel`
    -   `created_at`: datetime - assign with the current datetime when an instance is created
    -   `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
-   `__str__`: should print:  `[<class name>] (<self.id>) <self.__dict__>`
-   Public instance methods:
    -   `save(self)`: updates the public instance attribute  `updated_at`  with the current datetime
    -   `to_dict(self)`: returns a dictionary containing all keys/values of  `__dict__`  of the instance:
        -   by using  `self.__dict__`, only instance attributes set will be returned
        -   a key  `__class__`  must be added to this dictionary with the class name of the object
        -   `created_at`  and  `updated_at`  must be converted to string object in ISO format:
            -   format:  `%Y-%m-%dT%H:%M:%S.%f`  (ex:  `2017-06-14T22:31:03.285259`)
            -   you can use  `isoformat()`  of  `datetime`  object
        -   This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our  `BaseModel`

Essentially, other classes in the project will inherit from the  **BaseModel**  class:
## `User` class

-   `models/user.py`
-   Public class attributes:
    -   `email`: string - empty string
    -   `password`: string - empty string
    -   `first_name`: string - empty string
    -   `last_name`: string - empty string
    - 
## `State`  (`models/state.py`):
    -   Public class attributes:
        -   `name`: string - empty string
## `City`  (`models/city.py`):
    -   Public class attributes:
        -   `state_id`: string - empty string: it will be the  `State.id`
        -   `name`: string - empty string
## `Amenity`  (`models/amenity.py`):
    -   Public class attributes:
        -   `name`: string - empty string
## `Place`  (`models/place.py`):
    -   Public class attributes:
        -   `city_id`: string - empty string: it will be the  `City.id`
        -   `user_id`: string - empty string: it will be the  `User.id`
        -   `name`: string - empty string
        -   `description`: string - empty string
        -   `number_rooms`: integer - 0
        -   `number_bathrooms`: integer - 0
        -   `max_guest`: integer - 0
        -   `price_by_night`: integer - 0
        -   `latitude`: float - 0.0
        -   `longitude`: float - 0.0
        -   `amenity_ids`: list of string - empty list: it will be the list of  `Amenity.id`  later
## `Review`  (`models/review.py`):
    -   Public class attributes:
        -   `place_id`: string - empty string: it will be the  `Place.id`
        -   `user_id`: string - empty string: it will be the  `User.id`
        -   `text`: string - empty string


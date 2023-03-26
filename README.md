<div align="center">
  <h1>HBNB - The Console <img src="https://i.imgur.com/elr4ah9.png" width=55 align=center> </h1>
  <h4>
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2#repository-content">Content</a>
    •
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2#usage">Usage</a>
    •
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2#examples">Examples</a>
    •
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2#tests">Tests</a>
  </h4>
</div>

<img align="center" src="https://i.imgur.com/MQq3ABc.png" alt="Logo">

## Description

This repository contains version 2 of a project to build a clone of the AirBnB website. This version implements a back-end interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage, using a JSON serialization system or using MySQL as the database.

<img src="https://i.imgur.com/4H442BZ.png" alt="Structure">

---

## Repository Content

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [`AUTHORS`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [`/tests`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/tree/master/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [`/models/base_model.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [`/models/base_model.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [`/models/engine/file_storage.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [`/models/__init__.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/__init__.py) [`/models/base_model.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [`console.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [`console.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [`console.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/console.py) [`/models/engine/file_storage.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [`/models/user.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [`/models/user.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/user.py) [`/models/place.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/place.py) [`/models/city.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/city.py) [`/models/amenity.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/amenity.py) [`/models/state.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/state.py) [`/models/review.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [`console.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/console.py) [`/models/engine/file_storage.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
| 11. Console 2.0 | [`console.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/console.py) [`/models/engine/db_storage.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/models/engine/db_storage.py) [`/models/*`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/tree/master/models) | DBStorage implementation to manage storage by MySQL as a database |
<br>

## Usage

1. First clone this repository.

3. Once the repository is cloned, locate the [`console.py`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/console.py) file and run it as follows to manage JSON storage (FileStorage):
```sh
$ ./console.py
```
Or to manage the storage with the MySQL database (DBStorage) first run the [`setup_mysql_dev.sql`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/setup_mysql_dev.sql) file to set up the MySQL environment:
```sh
$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
```
Then run the console with this command to pass the necessary environment variables:
```sh
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>

## Examples

<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>

## Tests

To test all the functionality, several tests were created using the `unittest` module.
To test the code using FileStorage as storage (JSON):
```sh
$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
```
To test the code using DBStorage as storage (MySQL) you must first configure the MySQL environment with the [`setup_mysql_dev.sql`](https://github.com/Juanesduque1/holbertonschool-AirBnB_clone_v2/blob/master/setup_mysql_test.sql) file, like this:
```sh
cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
```
And to run the tests with this command:
```sh
HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
```

<br>

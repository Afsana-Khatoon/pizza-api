# pizza-api

Fistly pull the code and connect the Django project's(name: pizzaproject) database with your MongoDB Compass
Create a new database on the MongoDB Compass:
  The database name on MongoDB Compass = mongodatabase
  The collection name on MongoDB Compass = mongocollection
  
Install all the dependencies from Requirement.txt

To run the project, run the command-

python manage.py runserver

All the data inside the database can be accessed from the django admin panel:

Username = afsana

Password = root@12345

This the Djnago admin panel:
Reference image - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issue-886972323

In order to add extra type, size or topping, select the model in which you want to add data. Click on add button, write the name of the field and click on save.
The field will be added under that model.

APIs:
Open Postman-


1. To create pizza of a regular size or square size-

url = http://127.0.0.1:8000/create

method = POST

Then in the request body add the data of new pizza instance which you wanted to create. Choose the text mode to JSON, and send the request.

Reference image - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838363214

Note: The name of the key values should be same with the name of the instances of Pizaa model(i.e; type, size and topping) and the value for the key should be same with the
option which we have created in the database. Any incorrect data input will throw an error.
After sending the request new pizza instance will be created and stored in the database.

Reference image - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838377966


2. To see all the data about all pizza instances-

URL = http://127.0.0.1:8000/all_pizza_list

method = GET

Then send the request.

Reference image - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838328162

It will return all the data about all the pizza instances-

Reference image - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838336179


3. To filter the list of pizza-

URL = http://127.0.0.1:8000/pizza_list/filtered

method = GET

Now under the Params section add the values of both KEY and VALUE fields and then send the request.

Reference image - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838397532

This will filter the list according to the query parameters-

Reference image - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838399920

We can also filter on only one parameter, i.e; either type or size

Reference image - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838403862


4. To update the pizza instance-

URL = http://127.0.0.1:8000/update/3 (Here 3 is the id of the pizza instance which we wanted to update)

method = POST

Then in the request body change the data of the field you wanted to update and choose the mode of the text as JSON.

Reference image- https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838419891

Then send the request and the data will be updated.

Reference image - 

Before update - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838431532

After update - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838432296


5. To delete a pizza instance-

URL = http://127.0.0.1:8000/delete/13 (Here 13 is the id of the pizza instance which we wanted to delete)

method = DELETE

Then send the request and the pizza instance with the id 13 will be deleted.

Reference image - https://github.com/Afsana-Khatoon/pizza-api/issues/1#issuecomment-838441312

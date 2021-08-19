# ticketing_tool
Ticketing tool by Surendra

Steps to bring up django server:

1. Make migrations
$ docker-compose run ticketing python manage.py makemigrations
$ docker-compose run ticketing python manage.py migrate

2. Create super user
$ docker-compose run ticketing python manage.py createsuperuser
provide username and password

3. Bring up services
$ docker-compose up
$ docker-compose up postgres
$ docker-compose up ticketing

4. Launch admin page
http://127.0.0.1:8000/admin/

5. Create Groups for providing permissions through admin page
a. Admin - to allow permissions to do CRUD operations on model - Project
b. Project Manager - to allow permissions to do CRUD operations on model - Sprint

6. Add users to these groups and also select the user to be staff



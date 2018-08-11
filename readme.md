# API Python Example
This is a simple API developed in Python as a requirement of a selection process for employment.

It's only a compiled of several tutorials I found out when I was developing because I've never had developed in Python before.

And guess what? I don't get the job. So don't take this as a "best practice" example.

## Setting up the project
*All the steps are after clonning the repository.*

As I said before in this `readme` I've never had developed in python before so I will say here how I'm doing to execute the project. Feel free to sent me a message of a better way to do.
All the dependencies of the project are listed in the file `requirements.txt`.

First of all we will create and enter in our environment, to do so lets use the follow command line:
```
$ python3.6 -m venv env
$ source env/bin/activate
```

After that we will install the dependencies:
```
(env) $ pip install django==2.1
(env) $ pip install djangorestframework==3.8.2
```

## Executing the migrations and creating the admin user of Django
All things setted up we can run the migrations and create the admin user

#### Migrations
```
(env) $ python manage.py migrate
```

#### Creating user
```
(env) $ python manage.py createsuperuser
```

## Executing tests
The tests are one of the points to be improved but you can execute them by using the following

```
(env) $ python manage.py test
```
## Executing the project
```
(env) $ python manage.py runserver
```
The server runs in `http://127.0.0.1:8000`.

## Routes
####
`[GET] /admin`: Access to the admin of Django `http://127.0.0.1:8000/admin`

`[GET | POST] /employee`: Access the endpoint of employee `http://127.0.0.1:8000/employee`

`[GET | DELETE] /employee/{id}`: Access the endpoint of employee with an specifc identification code `http://127.0.0.1:8000/employee/{id}`

## Why I kept the example

Even that I didn't get the job as I said before the guys that analysed my code was very nice and give me the points to be improved (as a matter of fact this `readme` itself is one those points) so I still intend to improve this code as soon as I have time and more knowledge to do so.
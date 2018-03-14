Run project
===========

Working with Docker
-------------------

prepare project
```bash
$ docker-compose build
```

run project:
```bash
$ docker-compose up
```

add admin user:
```bash
$ docker-compose run --entrypoint "python /opt/class_project/manage.py createsuperuser" class_project
```

Working with VirtualEnv
-----------------------

prepare project
```bash
$ virtualenv venv
$ source venv/bin/activate
$ python ./manage.py migrate
```
run project:
```bash
$ python ./manage.py runserver
```

add admin user:
```bash
$ python ./manage.py createsuperuser
```

Auhtorisation
=============

Project has 2 authoristion methods:
- BasicHTTPAuthoristion
- SessionAuthentication

URLs
====

Array GET params example:
`/school-api/teachers/?classes=1,2,3`

Teachers
--------

`GET /school-api/teachers/`

Get teachers, public method

GET parameters for filtering:
- username
- first_name
- last_name
- specialisations (Array)
- classes (Array)

`POST /school-api/teachers/`

Create new teacher, only Admin can add teachers

`GET /school-api/teachers/<teacher_id>/`

Get teacher by <teacher_id>, public method 

`PUT /school-api/teachers/<teacher_id>/`

Update teacher by <teacher_id>, teacher can update self data and Admin can do it too

`DELETE /school-api/teachers/<teacher_id>/`

Delete teacher by <teacher_id>, teacher can delete self data and Admin can do it too

Specialisations
---------------

`GET /school-api/specialisations/`

Get specialisations, public method

GET parameters for filtering:
- name
- classes (Array)
- teachers (Array)

`POST /school-api/specialisations/`

Create new specialisation, only Admin can add specialisations

`GET /school-api/specialisations/<specialisation_id>/`

Get specialisations by <specialisation_id>, public method

`PUT /school-api/specialisations/<specialisation_id>/`

Update specialisation by <specialisation_id>, only Admin can update specialisations

`DELETE /school-api/specialisations/<specialisation_id>/`

Delete specialisation by <specialisation_id>, only Admin can delete specialisations


Classes
-------

`GET /school-api/classes/`

Get classes, public method

GET parameters for filtering:
- name
- description
- teachers (Array)
- specialisations (Array)
- students (Array)

`POST /school-api/classes/`

Create new class, teacher or Admin can do it

`GET /school-api/classes/<class_id>/`

Get class by <class_id>, public method

`PUT /school-api/classes/<class_id>/`

Update class by <class_id>, teacher or Admin can do it

`DELETE /school-api/classes/<class_id>/`

Delete class by <class_id>, teacher or Admin can do it


Students
--------

`GET /school-api/students/`

Get students

GET parameters for filtering:
- username
- first_name
- last_name
- classes (Array)

`POST /school-api/students/`

Create new student, public method

`GET /school-api/students/<student_id>/`

Get student with <student_id>, public method

`PUT /school-api/students/<student_id>/`

Update student with <student_id>, student can update self data and Admin can do it too

`DELETE /school-api/students/<student_id>/`

Delete student with <student_id>, student can delete self data and Admin can do it too

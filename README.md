# Kane's Image Editor

This project is a django-based webapp that makes use of Python's imaging library PIL to apply filters to a user updated image

## Getting Started

Make sure you have python installed on your system

### Installing packages

Make sure you have all the packages installed by using:

```
pip install -r requirements.txt
```

### Launching the webapp

Make sure you are in the project directory, then:

```
python manage.py makemigrations
```

To make sure all models are migrated:

```
python manage.py makemigrate
```

Then, to start:

```
python manage.py runserver
```

and go to http://localhost:8000/ on a browser tab to use the webapp

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [PIL](https://pillow.readthedocs.io/en/stable/) - Python's Imaging Library

## Authors

* **Ahmad Afiquddin Bin Ahmad** - *Initial work* - [Ahmad Afiquddin](https://github.com/ahmad-afiquddin)


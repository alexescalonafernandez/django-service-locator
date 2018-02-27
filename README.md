# django-service-locator
Django application that allows the use of a light implementation of the [service locator pattern](https://en.wikipedia.org/wiki/Service_locator_pattern).

## Goals
* Supply the service_locator command as a [custom django app command](https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/), which will generate the [providers](https://en.wikipedia.org/wiki/Service_provider_interface) configuration.
* Import the generated [providers](https://en.wikipedia.org/wiki/Service_provider_interface) configuration when the django app is ready.

## Getting Started
### Prerequisites
* Python version: >= 3.4
* [setuptools](https://pypi.python.org/pypi/setuptools)
* [setuptools-markdown](https://pypi.python.org/pypi/setuptools-markdown)
* [service-locator](https://github.com/alexescalonafernandez/service-locator.git)
* [django](https://docs.djangoproject.com/en/2.0/topics/install/)

### Installing
```
git clone https://github.com/alexescalonafernandez/django-service-locator.git
cd django-service-locator
python setup.py sdist
cd dist
pip install django-service-locator-1.0.tar.gz
```

### How to use it in django projects?
1) In requirements.txt add
```
service-locator==1.0
django-service-locator==1.0
```

2) In settings.py **INSTALLED_APPS** variable, add *django_service_locator* app.
```
INSTALLED_APPS = [
    ...,
    'django_service_locator',
    ...,
]
```

3) Use [service-locator](https://github.com/alexescalonafernandez/service-locator.git) library in your code.

4) Run the **service_locator** *command* for generating the [providers](https://en.wikipedia.org/wiki/Service_provider_interface) configuration files. 
```
python manage.py service_locator
```

5) Test your project
```
python manage.py runserver
```

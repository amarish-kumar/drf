# drf (Django rest framework)

A repository that contains the code for RESTful web api.

#### What is Django rest framework?

Django REST framework is a powerful and flexible toolkit for building Web APIs.

| Some reasons we might want to use REST framework |
| -------------------------------------------------|
| The [Web browsable API](http://restframework.herokuapp.com/) is a huge usability win for your developers. |
| [Authentication policies](http://www.django-rest-framework.org/api-guide/authentication/) including packages for [OAuth1a](http://www.django-rest-framework.org/api-guide/authentication/#django-rest-framework-oauth) and [OAuth2](http://www.django-rest-framework.org/api-guide/authentication/#django-oauth-toolkit). |
| [Serialization](http://www.django-rest-framework.org/api-guide/serializers/) that supports both [ORM](http://www.django-rest-framework.org/api-guide/serializers/#modelserializer) and [non-ORM](http://www.django-rest-framework.org/api-guide/serializers/#serializers) data sources. |
| Customizable all the way down - just use [regular function-based views](http://www.django-rest-framework.org/api-guide/views/#function-based-views) if you don't 
need the [more](http://www.django-rest-framework.org/api-guide/generic-views/) [powerful](http://www.django-rest-framework.org/api-guide/viewsets/) features. |
| [Extensive documentation](http://www.django-rest-framework.org/), and [great community support](https://groups.google.com/forum/?fromgroups#!forum/django-rest-framework). |
| Used and trusted by internationally recognised companies including [Mozilla](https://www.mozilla.org/en-US/about/), [Red Hat](https://www.redhat.com/en), [Heroku](https://www.heroku.com/), and [Eventbrite](https://www.eventbrite.co.uk/about/). |

#### Requirements

| Language/Framework | Version(s) |
| ------------------------------- |
| Python | 2.7, 3.2, 3.3, 3.4, 3.5 |
| Django | 1.8, 1.9, 1.10 |

#### Let's start

1. mkdir DrfProject

2. cd DrfProject

3. virtualenv vir_env

4. source ./vir_env/bin/activate  (on Linux, MAC OS X)
	
.\vir_env\Scripts\activate (on Windows)

5. pip install Django==1.8

6. django-admin.py startproject RestApiProj

7. mv RestApiProj src  (on Linux, MAC OS X)

ren RestApiProj src (on Windows)

8. cd src

9. python manage.py startapp SensorApp

10. python manage.py migrate

11. python manage.py createsuperuser  (provide username, email, password with confirmation)

11. pytohn manage.py runserver  



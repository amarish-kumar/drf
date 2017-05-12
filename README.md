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
| ------------------ | ---------- |
| Python | 2.7, 3.2, 3.3, 3.4, 3.5 |
| Django | 1.8, 1.9, 1.10 |

#### Let's start


| Language/Framework | Version(s) |
| ------------------ | ---------- |
| Python | 2.7, 3.2, 3.3, 3.4, 3.5 |
| Django | 1.8, 1.9, 1.10 |

#### Let's start

| SNo | Command |
| --- | ------- |
| 1 | mkdir DrfProject |
| 2 | cd DrfProject |
| 3 | virtualenv vir_env |
| 4 | source ./vir_env/bin/activate  (on Linux, MAC OS X) <br><br>.\vir_env\Scripts\activate (on Windows) | 
| 5 | pip install Django==1.8 (required) |
| 6 | django-admin.py startproject RestApiProj |
| 7 | mv RestApiProj src  (on Linux, MAC OS X) <br>ren RestApiProj src (on Windows) |
| 8 | cd src |
| 9 | python manage.py startapp SelfTrialApp  (I will use this app later) |
| 10 | python manage.py migrate |
| 11 | python manage.py createsuperuser  (provide username, email, password with confirmation) |
| 12 | pytohn manage.py runserver 6724 |
| 13 | pip install djangorestframework |
| 14 | pip install markdown       (Markdown support for the browsable API, optional) |
| 15 | pip install django-filter  (Filtering support, optional) |
| 16 | Add **'rest_framework'** to **'INSTALLED_APPS'** in settings.py |
| 17 | cd .. |
| 18 | pip freeze > pip-requirements.txt |
| 19 | Add the following to **RestApiProj/settings.py** |
| 20 | Finally Paste the following code to **RestApiProj/urls.py** |
| 21 | cd src	(moving to the directory where the manage.py is, as we are in drf-git directory) |
| 22 | python manage.py runserver <br>
Now visit [http://127.0.0.1:8000/users/](http://127.0.0.1:8000/users/) |


#### RestApiProj/settings.py

```python
#Global settings for Rest framework are kept in a single configuration dictionary
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
``` 

#### RestApiProj/urls.py

```python
from django.conf.urls import include, url
from django.contrib import admin

# Django restframework
from django.contrib.auth.models import User
from rest_framework import viewsets, routers, serializers

# ..............Serializers, Viewsets & Routers................

# Serializers define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		 model = User 
		 fields = ("url", "username", "email", "is_staff")

# Viewsets define the view behaviour
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


#....................urlpatterns...............................
# urlpatterns should be in the bottom of the above code
urlpatterns = [
    # Examples:
    # url(r'^$', 'RestApiProj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # my urls
    url(r"^", include(router.urls)),
    url(r"^selftrial/auth/", include("rest_framework.urls", namespace="rest_framework")),

]
```


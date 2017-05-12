from django.conf.urls import include, url
from django.contrib import admin

# Django restframework
from django.contrib.auth.models import User
from rest_framework import viewsets, routers, serializers
from SelfTrialApp.viewsets import StudentViewSet, PrimaryScoreViewSet, PostViewSet


# User: Serializers define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		 model = User 
		 fields = ("url", "username", "email", "is_staff")

# User: Viewsets define the view behaviour
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r"students", StudentViewSet)
router.register(r"primary-scores", PrimaryScoreViewSet)
router.register(r"posts", PostViewSet)

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
from rest_framework import viewsets

from .serializers import StudentSerializer, PrimarySchoolScoreSerializer, PostSerializer
from .serializers import HighSchoolScoreSerializer 
from .models import Student, PrimarySchoolScore, Post, HighSchoolScore


class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class PrimarySchoolScoreViewSet(viewsets.ModelViewSet):
	queryset = PrimarySchoolScore.objects.all()
	serializer_class = PrimarySchoolScoreSerializer

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class HighSchoolScoreViewSet(viewsets.ModelViewSet):
	queryset = HighSchoolScore.objects.all()
	serializer_class = HighSchoolScoreSerializer






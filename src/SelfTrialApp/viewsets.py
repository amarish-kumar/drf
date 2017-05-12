from rest_framework import viewsets

from .serializers import StudentSerializer, PrimaryScoreSerializer, PostSerializer
from .models import Student, PrimaryScore, Post

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class PrimaryScoreViewSet(viewsets.ModelViewSet):
	queryset = PrimaryScore.objects.all()
	serializer_class = PrimaryScoreSerializer

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer




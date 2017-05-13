from .models import Student, PrimaryScore, Post
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	""" Serializer of Student"""
	class Meta:
		model = Student
		fields = "__all__"

class PrimaryScoreSerializer(serializers.HyperlinkedModelSerializer):
	""" Serializer of PrimaryScore """
	class Meta:
		model = PrimaryScore
		fields = "__all__" 

class PostSerializer(serializers.HyperlinkedModelSerializer):
	""" Serializer of Post """
	class Meta:
		model = Post
		fields = "__all__"


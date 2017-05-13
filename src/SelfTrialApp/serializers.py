from .models import Student, PrimarySchoolScore, Post, HighSchoolScore
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	""" Serializer of Student"""
	class Meta:
		model = Student
		fields = "__all__"

class PrimarySchoolScoreSerializer(serializers.HyperlinkedModelSerializer):
	""" Serializer of PrimaryScore """
	class Meta:
		model = PrimarySchoolScore
		fields = "__all__" 

class PostSerializer(serializers.HyperlinkedModelSerializer):
	""" Serializer of Post """
	class Meta:
		model = Post
		fields = "__all__"

class HighSchoolScoreSerializer(serializers.HyperlinkedModelSerializer):
	""" Serializer for HighSchoolScore """
	class Meta:
		model = HighSchoolScore
		fields = "__all__"



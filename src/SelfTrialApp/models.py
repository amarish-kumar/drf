from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
	""" A class that defines the structure of Student object """

	fullname = models.CharField(max_length=50, blank=False)
	age = models.PositiveIntegerField(blank=False)
	roll_no = models.PositiveIntegerField(blank=False)
	branch = models.CharField(max_length=50, blank=False)

	def __unicode__(self):
		return self.fullname

class PrimaryScore(models.Model):
	""" 
		A class that defines the structure of Primary Score of all the subjects.
		The structure can be different for different schools.

		This is what I studied in kg1 to 5th(except 2nd as I directly moved to 3rd after 1st).
	"""
	fullname = models.ForeignKey("Student", on_delete=models.CASCADE)
	mathematics = models.PositiveIntegerField(blank=False)
	hindi = models.PositiveIntegerField(blank=False)
	english =  models.PositiveIntegerField(blank=False)
	science =  models.PositiveIntegerField(blank=False)
	environment =  models.PositiveIntegerField(blank=False)
	
	def __unicode__(self):
		# self.fullname.fullname
		return str(self.fullname)  

class Post(models.Model):
	""" A model that defines the structure of Post"""

	title = models.CharField(max_length=50, blank=False)
	description = models.TextField()
	pic = models.URLField(max_length=1000) #default max_length is 200
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	posted_by = models.ForeignKey(User, on_delete=models.CASCADE) # "User" => won't work

	def __unicode__(self):
		return self.title

class CommonScore(models.Model):
	""" A base class that defines the sturcture of common subjects for students """

	fullname = models.ForeignKey("Student", on_delete=models.CASCADE)
	hindi = models.PositiveIntegerField(blank=False)
	english = models.PositiveIntegerField(blank=False)
	mathematics = models.PositiveIntegerField(blank=False)

class HighScore(CommonScore):
	""" A class that inherits from CommonScore"""

	social_science = models.PositiveIntegerField(blank=False)
	environment = models.PositiveIntegerField(blank=False)
	sanskrit = models.PositiveIntegerField(blank=False)

	# def __init__(self):
	# 	  super(CommonScore, self).__init__()

	def __unicode__(self):
		return "Subject%d"%(self.id)




		
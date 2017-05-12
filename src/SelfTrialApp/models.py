from django.db import models

class Student(models.Model):
	""" A class that defines the structure of Student object"""

	fullname = models.CharField(max_length=50, blank=False)
	age = models.PositiveIntegerField(blank=False)
	roll_no = models.PositiveIntegerField(blank=False)
	branch = models.CharField(max_length=50, blank=False)

	def __unicode__(self):
		return self.fullname


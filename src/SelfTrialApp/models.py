from django.db import models

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


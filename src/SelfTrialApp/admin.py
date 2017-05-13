from django.contrib import admin
 
from .models import Student, PrimarySchoolScore, Post, HighSchoolScore

admin.site.register(Student)
admin.site.register(PrimarySchoolScore)
admin.site.register(Post)
admin.site.register(HighSchoolScore)


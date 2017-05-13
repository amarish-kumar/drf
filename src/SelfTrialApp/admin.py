from django.contrib import admin
 
from .models import Student, PrimaryScore, Post, HighScore

admin.site.register(Student)
admin.site.register(PrimaryScore)
admin.site.register(Post)
admin.site.register(HighScore)


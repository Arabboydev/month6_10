from django.contrib import admin

from .models import Speciality, Course, Teacher, Position


admin.site.register(Speciality)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Position)
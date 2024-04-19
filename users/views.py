from django.shortcuts import render
from django.views import View
from course.models import Course, Speciality, Teacher
from blog.models import Blog


class LondingPageView(View):
    def get(self, request):
        specialitys = Speciality.objects.all()
        courses = Course.objects.all()
        teachers = Teacher.objects.all()
        blogs = Blog.objects.all()
        context = {
            "specialitys" : specialitys,
            "courses" : courses,
            "teachers" : teachers,
            "blogs" : blogs,

        }
        return render(request, "main/index.html", context)






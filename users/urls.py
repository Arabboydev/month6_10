from django.shortcuts import render
from django.views import View
from course.models import Course, Speciality



class LondingPageView(View):
    def get(self, request):
        specialitys = Speciality.objects.all()
        context = {
            "specialitys" : specialitys
        }
        return render(request, "main/index.html", context)


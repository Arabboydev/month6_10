from django.shortcuts import render
from django.views import View
from .models import Blog


class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            "blogs" : blogs
        }
        return render(request,"main/blog.html",context)



# Create your views here.

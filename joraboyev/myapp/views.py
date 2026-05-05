from django.shortcuts import render

from .models import Blogs

def about(request):
    blogs = Blogs.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'about.html', context)

from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog


def home(request):
    # now fetch the categories to display the all categories
    # we gete the categories from the context_processors
    featured_post = Blog.objects.filter(is_featured=True)
    context = {
        "featured_post" : featured_post,
    }
    
    # now show featured post
    return render(request,'home.html',context)
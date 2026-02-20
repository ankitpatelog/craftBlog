from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog


def home(request):
    # now fetch the categories to display the all categories
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True)
    context = {
        "categories" : categories,
        "featured_post" : featured_post,
    }
    
    # now show featured post
    return render(request,'home.html',context)
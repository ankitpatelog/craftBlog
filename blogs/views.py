from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Blog,Category
# Create your views here.

def posts_by_category(request,category_id):
    # fetch the post that belongs to the category id it belongs
    # means browser cat_id shoild be same as the blog cat_id and fetch that post
    # use try/catch when we have to do some custom actions when the object not found
    try:
        post = Blog.objects.filter(status='Published',category_id=category_id)
        
        if not post.exists():
            return redirect('home')
    except:
        return redirect('home')
      
    # use get_object_or_404 when we want to redirect to 404 page when the apge not found
    # post = get_object_or_404(Category,pk=category_id)
    context = {
        "post" : post,
    }
    
    return render(request,'posts_by_category.html',context)
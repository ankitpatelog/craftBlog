from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Blog,Category,Comment
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


def blog(request,slug):
    single_blog = Blog.objects.filter(status='Published', slug=slug)
    if request.method=='POST':
        # handle the post request for the comment upload for the particular slug
        comment = comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        
    # else fetch the comment for this blog slug and pass in the form of context into the html template
    prev_comment  = comment.objects.filter(blog=single_blog)
    
    context = {
        'comment' : prev_comment,
        'blog': single_blog
    }
    
    return render(request,'blog.html',context)
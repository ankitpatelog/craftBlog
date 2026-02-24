from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Blog,Category,Comment
from .form import registrationform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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


def register(request):
    if request.method == 'POST':
        # pass the form data stored into the request.post , then check for is_valid 
        # if valid then save into the data base and then redirect
        form = registrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = registrationform()
        
    context = {
        'form':form,
    }
    
    return render(request,'register.html',context)

def login(request):
    if request.method == 'POST':
        # we will use defalut authentication form by django
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            # if form is valid take the user enterd fields
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # now take the auth from djanog
            user = auth.authenticate(username=username,password=password)
            
            if user is not None:
                auth.login(request,user)
            return redirect('home')
    
    
    # if it was not post request just view page then show the form 
    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'login.html',context) 


def logout(request):
    auth.logout()
    return redirect('home')
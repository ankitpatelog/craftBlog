from django.shortcuts import render
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from form import BlogFform
from django.template.filter import slugify

# Create your views here.

# it takess the loign_url to send the user when the user is not authenticated
@login_required(login_url='login')
def dashboard(request):
    cat_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    
    context = {
        'cat_count': cat_count,
        'blog_count': blog_count,
    }
    
    return render(request,'dashboard/dashboard.html',context)


def categories(request):
    return render(request,'dashboard/categories.html')

# deleting category blog form dashboard section from frontend
# def delete_category(request,pk):
#     category = get_object_or_404(Category,pk)
#     category.delete()
#     return redirect('categoreies')


def post(request):
    # post.html contains all the post
    posts = Blog.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request,'dashboard/post.html',context)

def add_post(request):
    if request.method == 'POST':
        # save data into database with the slug and and the default authod as the editor who is logged in the website
        form = BlogFform(request.POST,request.FILES)
        if form.is_valid():
            form.author = request.user
            # first take the title from the post
            title = form.cleaned_data['title']
            form.slug = slugify(title)
            form.save()
            return redirect('post') 
    form =  BlogFform()
    context = {
        'form': form,
    }
    
    return render(request,'dashboard/add_post.html',context)
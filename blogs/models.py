from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Category model
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category_name
    
# Blog model
STATUS_CHOICES = (
    (0,"Draft"),
    (1,"Published")
)  

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=1000)
    status = models.IntegerField(choices=STATUS_CHOICES,default=0)
    is_featured = models.IntegerField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
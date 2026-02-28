from django import forms
from blogs.models import Blog

class BlogFform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title,category,featured_image,blog_body,short_description,status,is_featured')
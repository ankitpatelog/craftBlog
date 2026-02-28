from django.urls import path
from . import views

urlpattern = [
    path(''.views.dashboard,name='dashboard'),
    path('categories/',views.categories,name='categories'),
    
    # blog post crud
    path('posts/',views.post,name= 'post'),
    path('posts/add',views.add_post,name='add_post')
]
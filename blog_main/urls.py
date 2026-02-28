
from django.contrib import admin
from django.urls import path,include
from . import view

from django.conf import settings
from django.conf.urls.static import static 
from blogs import views as BlogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home,name='home'),
    path('category/',include('blogs.url')),
    # this one to show the blog per slug
    path('blog/',include('blogs.url')),
    path('blog/<slug:slug>/',include(BlogViews.blog)),
    path('register/',view.register,name='register'),
    path('login/',view.login,name='login'),
    path('logout/',view.logout,name='logout'),
    # url for dashboard
    path('dashboard',include('dashboard.url'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.user, name='users'),
    path('blogs', views.post, name='blogs'),
    path('comments', views.comment, name='comments'),
    path('categories', views.category, name='categories'),
    path('blogs/blogdetails/<int:id>', views.blogdetails, name='blogdetails'),
]
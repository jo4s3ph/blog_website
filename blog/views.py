from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


def user(request):
    myuser = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
    'myuser': myuser,
    }
    return HttpResponse(template.render(context, request))


def post(request):
    blogs = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
    'blogs': blogs,
    }
    return HttpResponse(template.render(context, request))

def blogdetails(request, id):
  blogs = Post.objects.get(id=id)
  template = loader.get_template('blogdetails.html')
  context = {
    'blogs': blogs,
  }
  return HttpResponse(template.render(context, request))


def commentdetails(request, id):
  mycomments = Comment.objects.get(postId=id)
  template = loader.get_template('blogdetails.html')
  context = {
    'mycomments': mycomments,
  }
  return HttpResponse(template.render(context, request))



def comment(request):
    comments = Comment.objects.all().values()
    template = loader.get_template('comments.html')
    context = {
    'comments': comments,
    }
    return HttpResponse(template.render(context, request))



def category(request):
    categories = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
    'categories': categories,
    }
    return HttpResponse(template.render(context, request))


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

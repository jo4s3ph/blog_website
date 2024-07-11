from django.db import models



class User(models.Model):

    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=67)

def __str__(self):
    return f"{self.username}"




class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    category = models.CharField(max_length=255)
    date_published = models.DateField(auto_now=True)




class Comment(models.Model):

    postId = models.ForeignKey(to=Post , on_delete=models.CASCADE)
    userId = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    date_posted = models.DateField(auto_now=True)




class Category(models.Model):

    name = models.CharField(max_length=255)



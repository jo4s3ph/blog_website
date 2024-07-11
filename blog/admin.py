from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
  list_display = ("username", "email")
admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
  list_display = ("title", "content", "category", "date_published")
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
  list_display = ("content", "date_posted", "postId")
admin.site.register(Comment, CommentAdmin)


class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name",)
admin.site.register(Category, CategoryAdmin)

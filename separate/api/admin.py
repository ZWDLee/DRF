from django.contrib import admin
from .models import User, Books


@admin.register(User)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')

@admin.register(Books)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')

from django.contrib import admin
from .models import BlogPost, Comment

from django.db import models
from tinymce.widgets import TinyMCE


@admin.register(BlogPost)

class textEditorAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_status', 'created_time', 'updated_time')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('publish_status', 'created_time')
    search_fields = ['title', 'content']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


# admin.site.register(BlogPost, textEditorAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']

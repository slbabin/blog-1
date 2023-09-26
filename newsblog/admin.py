from django.contrib import admin
from .models import BlogPost

from django.db import models
from tinymce.widgets import TinyMCE


@admin.register(BlogPost)

class textEditorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


# admin.site.register(BlogPost, textEditorAdmin)

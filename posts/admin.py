from django.contrib import admin
from models import Post
from django.db.models import TextField
from ckeditor.widgets import CKEditorWidget


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created_at')
    formfield_overrides = {TextField: {'widget': CKEditorWidget()}}

admin.site.register(Post, PostAdmin)

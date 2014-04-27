from django.contrib import admin
from models import Tag


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'created_at']

admin.site.register(Tag, TagAdmin)

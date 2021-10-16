from django.contrib import admin
from .models import Blogpost

class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status','created_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blogpost, BlogpostAdmin)

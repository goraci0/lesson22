from django.contrib import admin

from .models import Article, Comment

# Register your models here.

admin.site.register(Article,site=admin.site)
admin.site.register(Comment,site=admin.site)

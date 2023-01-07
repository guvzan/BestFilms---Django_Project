from django.contrib import admin

from .models import *

admin.site.register(Film)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(BlogPost)
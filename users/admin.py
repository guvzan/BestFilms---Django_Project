from django.contrib import admin

from .models import *

admin.site.register(CustomUser)
admin.site.register(PagePost)
admin.site.register(Inbox)
admin.site.register(Message)

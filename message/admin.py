from django.contrib import admin

from .models import Message, UserMessage
admin.site.register(Message)
admin.site.register(UserMessage)

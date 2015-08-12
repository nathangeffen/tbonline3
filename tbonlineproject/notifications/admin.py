'''Admin interface registers Image model with admin.site. 
'''
from django.contrib import admin

from models import Notification, CommentNotification, Recipient


class NotificationRecipientInline(admin.TabularInline):
    model = Recipient


class NotificationAdmin(admin.ModelAdmin):
    inlines = [
        NotificationRecipientInline,
    ]

admin.site.register(Notification, NotificationAdmin)
admin.site.register(CommentNotification)
admin.site.register(Recipient)

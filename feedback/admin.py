from django.contrib import admin

# Register your models here.

from .models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_display=("feedback_content","date","ratings","feedback_status")
    
admin.site.register(Feedback,FeedbackAdmin)
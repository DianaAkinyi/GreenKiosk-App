from django.shortcuts import render, redirect
from .models import Notification
from .forms import NotificationUploadForm

def notification_details_views(request):
    if request.method == "POST":
        form = NotificationUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_details_views') 
    else:
        form = NotificationUploadForm()
    return render(request, 'notification/add_notification.html', {'form': form})

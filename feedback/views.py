from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackUploadForm

def feedback_details_views(request):
    if request.method == "POST":
        form = FeedbackUploadForm(request.POST)
        
        return redirect('product_list.html') 
    else:
        form = FeedbackUploadForm()
    return render(request, 'feedback/feedback_details.html', {'form': form})

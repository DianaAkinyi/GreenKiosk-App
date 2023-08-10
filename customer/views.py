from django.shortcuts import render

# Create your views here.
from  .models import Customer
from  .forms import CustomerUploadForm
# Create your views here.
def customer_details_views(request):
    if request.method=="POST":
     form=CustomerUploadForm(request.POST)
     if form.is_valid():
        form.save()
    else:
      form=CustomerUploadForm()
    return render(request,'customer/customer_detail.html',{'form':form})
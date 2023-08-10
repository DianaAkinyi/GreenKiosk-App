from .forms import CartUploadForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
# from .forms import CartForm

# ..........................
def add_to_cart(request):
    if request.method == 'POST':
        form = ProductCartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_detail_view')
    else:
        form = CartUploadFormForm()
    return render(request, 'cart/add_to_cart.html', {'form': form})


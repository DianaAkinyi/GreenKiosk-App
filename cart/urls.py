from django.urls import path
from .views import add_to_cart
# from.import views
urlpatterns= [
   
    path('cart/add_to_cart/', add_to_cart, name='add_to_cart'),
]
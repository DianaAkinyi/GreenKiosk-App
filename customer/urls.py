from django.urls import path;
from .views import customer_details_views
urlpatterns=[
path("customer/upload/",customer_details_views,name="customer_details_views"),
]







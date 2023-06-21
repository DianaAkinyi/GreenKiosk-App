from django.contrib import admin

# Register your models here.
from.models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_payment=("amount","payment_status","payment_date","method")



admin.site.register(Payment,PaymentAdmin)
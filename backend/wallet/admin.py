from django.contrib import admin
from .models import (
    CustomerWallet,
    PaymentMethod,
    PaymentTransaction,
    TaskerPaymentAccount,
    TaskerWallet,
)

admin.site.register(CustomerWallet)
admin.site.register(PaymentMethod)
admin.site.register(TaskerPaymentAccount)
admin.site.register(TaskerWallet)
admin.site.register(PaymentTransaction)

# Register your models here.

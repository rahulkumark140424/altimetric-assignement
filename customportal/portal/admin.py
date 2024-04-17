from django.contrib import admin
from .models import Customer, Plan
# Register your models here.



class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ("registration_date","plan_renewal_date",)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Plan)
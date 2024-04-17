from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("create_customer/", views.CreateCustomer.as_view(), name="create_customer"),
    path("change_plan/<int:customer_id>", views.PlanChange.as_view(), name="change_plan"),
    path("renew_plan/<int:customer_id>", views.RenewPlan.as_view(), name="renew_plan"),
]
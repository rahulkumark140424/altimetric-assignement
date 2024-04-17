from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.views import View
from .models import Customer, Plan
from .forms import CustomerForm, PlanChangeForm
from datetime import date


class Index(ListView):
    context_object_name = "customers"
    queryset = Customer.objects.all()
    template_name = "portal/index.html"

class CreateCustomer(View):
    form = CustomerForm
    template_name = "portal/create_customer.html"

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {"customer_form": form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

        return render(request, self.template_name, {"customer_form": form})
    

class PlanChange(View):
    form = PlanChangeForm
    template_name = "portal/change_plan.html"

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        customer_id = kwargs.get('customer_id')
        customerObj = get_object_or_404(Customer, pk=customer_id)
        form = self.form(request.POST)
        if form.is_valid():
            plan_id = request.POST.get("plan")
            planObj = Plan.objects.get(id=plan_id)
            customerObj.plan = planObj
            customerObj.plan_renewal_date = date.today()
            customerObj.save()
            return HttpResponseRedirect("/")

        return render(request, self.template_name, {"form": form})
    

class RenewPlan(View):
    template_name = "portal/renewal_success.html"
    def get(self, request, *args, **kwargs):
        
        customer_id = kwargs.get('customer_id')
        customerObj = get_object_or_404(Customer, pk=customer_id)
        msg=""
        if customerObj.plan:
            customerObj.plan_renewal_date=date.today()
            customerObj.save()
        else:
            msg="Please select a Plan first."
        return render(request, self.template_name,{"customer":customerObj, "msg":msg})
    
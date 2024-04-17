from django import forms
from .models import Customer, Plan

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ("registration_date", 'plan_renewal_date',)
    def clean(self):
 
        
        super(CustomerForm, self).clean()
         
        # extract the aadhar and mobile field from the data
        aadhar_num = self.cleaned_data.get('aadhar_num')
        mobile_number = self.cleaned_data.get('mobile_number')
 
        # conditions to be met for the aadhar and mobile length
        if len(aadhar_num) !=12:
            self._errors['aadhar_num'] = self.error_class([
                'Aadhar must be of 12 digits.'])
        if len(mobile_number) !=10:
            self._errors['mobile_number'] = self.error_class([
                'Mobile Must be of 10 digits.'])
 
        # return any errors if found
        return self.cleaned_data
        
class PlanChangeForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields=["plan"]
    def clean(self):
        super(PlanChangeForm, self).clean()
        plan = self.cleaned_data.get('plan')
        if not plan:
            self._errors['plan'] = self.error_class([
                'Please select a Plan.'])

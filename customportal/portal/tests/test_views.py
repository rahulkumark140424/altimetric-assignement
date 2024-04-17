import datetime
from django.test import TestCase  
from django.urls import reverse  
from portal.models import Customer, Plan



class ViesTestCase(TestCase):  
    def test_index(self):  
        response = self.client.get(reverse('index'))  
        self.assertEqual(response.status_code, 200)  

    def test_create_customer(self):
        response = self.client.get(reverse('create_customer'))
        self.assertEqual(response.status_code, 200) 

    def test_change_plan(self):
        plan = Plan.objects.create(name="plt", cost="365", validity="365",status=True)
        customer = Customer.objects.create(name="John Wick",dob=datetime.date(1984,4,13), email="john_wick@gmail.com",
                                       aadhar_num="123456742212",registration_date=datetime.date.today(),
                                       mobile_number="8456188864",plan=plan, plan_renewal_date=datetime.date.today())
        response = self.client.get(reverse('change_plan',args=[customer.id]))
        self.assertEqual(response.status_code, 200)
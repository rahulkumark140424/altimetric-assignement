from django.test import TestCase
from portal.models import Customer, Plan
import datetime

class CustomerTest(TestCase):
    def create_customer(self):
        plan = Plan.objects.create(name="plt", cost="365", validity="365",status=True)
        return Customer.objects.create(name="John Wick",dob=datetime.date(1984,4,13), email="john_wick@gmail.com",
                                       aadhar_num="123456742212",registration_date=datetime.date.today(),
                                       mobile_number="8456188864",plan=plan, plan_renewal_date=datetime.date.today())
    
    def test_customer_creation(self):
        c = self.create_customer()
        self.assertTrue(isinstance(c, Customer))
        self.assertEqual(c.__str__(), c.name)
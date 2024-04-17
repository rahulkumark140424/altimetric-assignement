from django.db import models
from datetime import date

PLAN_VALIDITY = [
    ("365", "365"),
    ("180", "180"),
    ("90", "90"),
]

PLAN_COST = [
    ("365", "365"),
    ("180", "180"),
    ("90", "90"),
    ]


PLAN_NAME = [
    ("plt", "Platinum365"),
    ("gld", "Gold180"),
    ("slv", "Silver90"),
]

class Plan(models.Model):
    name = models.CharField(max_length=3, choices=PLAN_NAME, blank=False, null=False)
    cost = models.CharField(max_length=3, choices=PLAN_COST, blank=False, null=False)
    validity = models.CharField(max_length=3, choices=PLAN_VALIDITY, blank=False, null=False)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.get_name_display()


class Customer(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    aadhar_num = models.CharField(max_length=12, blank=False, null=False)
    registration_date = models.DateField(auto_now_add=True)
    mobile_number = models.CharField(max_length=10, blank=False, null=False)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, blank=True, null=True)
    plan_renewal_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name

#admin
#admin@admin.com
#admin@1234

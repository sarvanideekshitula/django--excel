from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company_details(models.Model):
    Company_name = models.CharField(max_length=50)
    CTC = models.IntegerField()
    Date_of_visit = models.DateField()
    Eligibility = models.CharField(max_length=20)
    Branch = models.CharField(max_length=20)

    def __str__(self):
        return self.Company_name

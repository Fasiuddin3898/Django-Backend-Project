from unittest.util import _MAX_LENGTH as max_length
from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    phone_number =models.CharField(max_length=122)
    email_address = models.CharField(max_length=122)
    planning_which_country=models.CharField(max_length=122)
    qualification=models.CharField(max_length=122)
    tell_about_yourself=models.TextField(blank=True)

    def __str__(self):
        return self.full_name

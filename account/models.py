# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

ACCOUNT_TYPE = (
    ('driver', 'Driver'),
    ('client', 'Client')
)


class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?\d{10,12}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13)  # validators should be a list
    location = models.CharField(max_length=60)
    birth_date = models.DateField(null=True, blank=True)
    account_type = models.CharField(max_length=255, choices=ACCOUNT_TYPE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

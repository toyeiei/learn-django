from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=300, default='')
    company = models.CharField(max_length=300, default='')
    year = models.IntegerField(default=2021)


class Email(models.Model):
    email = models.CharField(max_length=300, default='')

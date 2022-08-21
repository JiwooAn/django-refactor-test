from django.db import models


# Create your models here.
class Check(models.Model):
    abc = models.CharField(max_length=10, null=True, blank=True)
    abc123 = models.CharField(max_length=1, null=True, blank=True)
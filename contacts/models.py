from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    coutry = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=10)
    contact_picture = models.URLField(null=True)
    is_favourite = models.BooleanField(default=False)
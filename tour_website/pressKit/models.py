from django.db import models

# Create your models here.

class shows(models.Model):
    name = models.CharField(max_length=50)
    local = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time_start = models.TimeField(auto_now=False, auto_now_add=False)
    time_end = models.TimeField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=15)
    description = models.CharField(max_length=2000)
    venue = models.CharField(max_length=25)
    ticket_link = models.CharField(max_length=250)
    def __str__(self):
        return str(self.name)

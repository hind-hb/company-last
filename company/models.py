from django.db import models
from django.dispatch import receiver

class Company(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    dec = models.CharField(max_length=500)
    company = models.ForeignKey(Company,related_name='department',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Employee(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    department = models.ForeignKey(Department,related_name='employee',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return (self.name+self.address)

# Create your models here.




from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    registration_date = models.DateField()
    registration_number = models.CharField(max_length=50)
    address = models.TextField()
    contact_person = models.CharField(max_length=100)
    departments = models.ManyToManyField('Department')

    def __str__(self):
        return str(self.name)
    
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    date_started = models.DateField()
    date_left = models.DateField(blank=True, null=True)
    duties = models.TextField()

    def __str__(self):
        return str(self.name)

# Create your models here.

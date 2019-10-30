from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def _str_(self):
        return (f'{self.last_name}, {self.first_name}')

class Page(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    url = models.CharField(max_length=40)

    def _str_(self):
        return self.title
    
class Loan(models.Model):
    name = models.CharField(max_length=30)
    loan = models.FloatField()
    deposit = models.FloatField()
    ltv = models.FloatField()
    term = models.DecimalField(max_digits=5, decimal_places=2)
    outstanding = models.FloatField()

    def _str_(self):
        return (f'Loan {self.name} of {self.loan}')
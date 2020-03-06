
from django.db import models
# This is comment

# From server to local

class Employee(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename= models.CharField(max_length=30)
    esal = models.IntegerField()

    def __str__(self):
        return self.ename

from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name=models.CharField(max_length=30)
    company=models.CharField(max_length=100)
    email=models.EmailField(max_length=30)
    contact=models.CharField(max_length=13)
    class Meta:
        db_table='client'

    def __str__(self):
        return self.name

class Project(models.Model):
    Projectname=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    startdate=models.DateField()
    enddate=models.DateField()
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    user=models.ManyToManyField(User)
    def __str__(self):
        return self.Projectname
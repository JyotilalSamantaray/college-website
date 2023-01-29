from django.db import models

class insertdata(models.Model):
    Student_Name= models.CharField(max_length=50)
    Father_Name= models.CharField(max_length=50)
    Mother_Name= models.CharField(max_length=50)
    Course_Name= models.CharField(max_length=10)
    Gender= models.CharField(max_length=10)
    Country_Code = models.IntegerField()
    Phone= models.IntegerField()
    Address = models.CharField(max_length=200)
    Email= models.CharField(max_length=50)
    Password= models.CharField(max_length=50)

class mark(models.Model):
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    DM = models.IntegerField()
    CSA = models.IntegerField()
    CDS = models.IntegerField()
    DE = models.IntegerField()
    OS = models.IntegerField()
    Roll = models.IntegerField()
from django.db import models

# Create your models here.
class Information(models.Model):
    department=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    startdate=models.CharField(max_length=200)
    enddate=models.CharField(max_length=200)
    duration=models.CharField(max_length=200)
    participants=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    semister=models.CharField(max_length=200)
    facultyname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    myfile=models.CharField(max_length=200)
    message=models.TextField(max_length=500)
    def __str__(self):
        return (self.myfile)


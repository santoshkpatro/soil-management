from django.db import models

class User_Login(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=10)
    emailid = models.CharField(max_length=200)
    username = models.CharField(max_length=100, primary_key=True)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=70)
    address = models.CharField(max_length=500)
    pin = models.CharField(max_length=6)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from ckeditor.fields import RichTextField
# Create your models here.

# models for the Profile for the user 
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=6) #user gender 
    lookingFor = models.CharField(max_length=6) # looking for gender 
    age =models.IntegerField() 
    phone =models.BigIntegerField() #phone number of the user 

    def __str__(self):
        return str(self.user)

    
    # model for the contact form for name email subject phone message

class Contact(models.Model):
        name=models.CharField(max_length=50)
        email=models.EmailField()
        subject =models.CharField(max_length=100)
        phone =models.BigIntegerField()
        message = models.TextField()

        def __str__(self):
            return str(self.name)

class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField()
    content=RichTextField()
    posted_date=models.DateTimeField(auto_now_add=True)




    


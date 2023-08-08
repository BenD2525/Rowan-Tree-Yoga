from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class Review(models.Model):
    '''Model which stores the website reviews.'''
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Enquiry(models.Model):
    '''Model which stores customer enquiries.'''
    email = models.EmailField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.title
    
class Image(models.Model):
    '''Model which stores gallery images.'''
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False) # Only one image can be featured at a time.

    def __str__(self):
        return self.description
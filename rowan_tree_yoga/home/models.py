from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Review(models.Model):
    '''Model which stores the website reviews.'''
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''Defines a redirect URL after editing/deleting.'''
        return reverse('home:reviews')
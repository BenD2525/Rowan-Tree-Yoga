from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('gallery', views.gallery, name='gallery'),
    path('contact_us', views.ContactUs.as_view(), name='contact_us'),
    path('classes', views.classes, name='classes'),
    path('reviews', views.reviews, name='reviews'),
]

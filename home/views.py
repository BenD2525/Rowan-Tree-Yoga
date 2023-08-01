from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render(request, 'home/about_us.html')

def gallery(request):
    return render(request, 'home/gallery.html')

def contact_us(request):
    return render(request, 'home/contact_us.html')

def classes(request):
    return render(request, 'home/classes.html')

def reviews(request):
    return render(request, 'home/reviews.html')

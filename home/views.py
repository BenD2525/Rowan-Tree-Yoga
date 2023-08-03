from django.shortcuts import render
from .models import Review

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
    ''' Returns the reviews page.'''

    serialized_reviews = []

    reviews = Review.objects.all()

    for review in reviews:
        serialized_reviews.append({
            "title": review.title,
            "content": review.content,
            "user": review.user,
            "created": review.created,
            "id": review.id,
        })

    context = {
        "reviews": serialized_reviews
        }
    return render(request, 'home/reviews.html', context)

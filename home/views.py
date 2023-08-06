from django.shortcuts import render, redirect
from django.views import View
from .models import Review, Enquiry
from .forms import EnquiryForm
from django.contrib import messages
from rowan_tree_yoga.settings import DEFAULT_FROM_EMAIL
from templated_email import send_templated_mail


def home(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render(request, 'home/about_us.html')

def gallery(request):
    return render(request, 'home/gallery.html')

class ContactUs(View):
    '''View which allows the user to contact the website.'''

    def get(self, request, *args, **kwargs):

        enquiry = Enquiry
        enquiry_form = EnquiryForm

        context = {
            'enquiry': enquiry,
            'enquiry_form': enquiry_form,
            'title': enquiry.title,
            'content': enquiry.content,
        }
        return render(request, 'home/contact_us.html', context)

    def post(self, request, *args, **kwargs):

        enquiry_form = EnquiryForm(data=request.POST)

        if enquiry_form.is_valid():
            obj = enquiry_form.save(commit=False)
            obj.save()
            send_templated_mail(
                template_name='contact_us',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[obj.email],
                context={'title': obj.title,
                         'content': obj.content,
                         },
            )
            messages.success(request, "Thanks for submitting an enquiry!")
        return redirect("home:home")

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

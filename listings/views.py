from multiprocessing import context
from django.shortcuts import render
from .models import Listing


# Create your views here.


def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    # Passing the context to the render function
    return render(request, 'listings/listings.html', context)


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')

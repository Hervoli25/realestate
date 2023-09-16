from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # Change '3' to the desired number of items per page
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')

    try:
        paged_listings = paginator.page(page)
    except PageNotAnInteger:
        paged_listings = paginator.page(1)
    except EmptyPage:
        paged_listings = paginator.page(paginator.num_pages)

    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # Your listing view logic here
    return render(request, 'listings/listing.html')


def search(request):
    # Your search view logic here
    return render(request, 'listings/search.html')

from django.shortcuts import render, redirect
from .models import Apartments
from django.contrib import auth
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    apartments = Apartments.objects.order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(apartments, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "apartments": page,
        "header_h1": "Квартири <span>для вас</span>",
        "header_p": "Головна >> Квартири для вас",
    }
    return render(request, "pages/apartments.html", context)


def apartment(request, apartment_id):
    apartment = get_object_or_404(Apartments, pk=apartment_id)
    context = {
        "apartment": apartment,
        "header_h1": "Квартири <span>для вас</span>",
        "header_p": "Головна >> Квартири для вас",
    }
    return render(request, "pages/apartment.html", context)

def search(request):
    return render(request, 'pages.search.html')

def favorite(request):
    if request.method == "POST":
        apartment_id = request.POST['apartment_id']
        if request.user != 'AnonymousUser':
            apartment=Apartments.objects.filter(id=apartment_id)
            filtered_apartment = apartment.filter(is_favorite=request.user)
            if filtered_apartment.count() == 0:
                apartment[0].is_favorite.add(request.user)
                apartment[0].save()
        else: return redirect('login')
    return redirect("/apartments/"+apartment_id)
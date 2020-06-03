from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('guarantee', views.guarantee, name="guarantee"),
    path('discounts', views.discounts, name="discounts"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('testimonials', views.testimonials, name="testimonials"),
    path('apartment', views.apartment, name="apartment"),
    path('we_offer', views.we_offer, name="we_offer"),
]

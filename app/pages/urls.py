from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('guarantee.html', views.guarantee, name="guarantee"),
    path('discounts.html', views.discounts, name="discounts"),
    path('contact_us.html', views.contact_us, name="contact_us"),
    path('testimonials.html', views.testimonials, name="testimonials")
]


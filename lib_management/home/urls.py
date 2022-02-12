from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('donate/', views.donate, name="donate"),
    path('donate/summary/', views.payment, name="donate_summary"),
    path('donate/success/', views.success, name="success"),
    path('check', views.check, name="check"),
]
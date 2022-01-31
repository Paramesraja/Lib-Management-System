from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('logout/', views.log_out, name="logout"),
    path('profile/', views.profile, name="profile"),
]

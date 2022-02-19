from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('logout/', views.log_out, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('view-book/', views.view_book, name="view_book"),
    path('add-book/', views.add_book, name="add_book"),
    path('renew/', views.renew, name="renew"),
]

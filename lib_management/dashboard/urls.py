from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('logout/', views.log_out, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('view-book/', views.view_book, name="view_book"),
    path('add-book/', views.add_book, name="add_book"),
    path('renew/', views.renew, name="renew"),
    path('view-damage/', views.view_damage_report, name="view_damage"),
    path('view-damage/send-mail', views.send_mail, name="send_mail"),
    path('report-damage/', views.report_damage, name="report_damage"),
]

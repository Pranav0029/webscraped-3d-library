from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("stu_log/", views.stu_log, name='stu_log'),
    path('', views.home, name='home'),
    path("first/", views.first, name='first'),
    path("lab_cat/", views.lab_cat, name='lab_cat'),
]
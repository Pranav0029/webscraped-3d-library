from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("lib_log/",views.lib_log,name='lib_log'),
    path("members/",views.members,name='members'),
    path("report/",views.report,name='report'),
]
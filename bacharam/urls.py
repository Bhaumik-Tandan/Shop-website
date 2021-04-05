from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('manage/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('t', views.ide, name='t'),
]

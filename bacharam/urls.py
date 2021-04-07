from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('manage/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('log', views.log, name='log'),
    path('reg', views.reg, name='reg'),
    path('proddet/', views.ProductList.as_view()),
    path('proddet/<str:pk>/',
         views.proddet, name='proddet'),
    path('t', views.ide, name='t'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_url = 'http://127.0.0.1:8000/SchroniskoAPI/'
urlpatterns = [
    path('stanowisko', views.StanowiskoList.as_view(), name='stanowisko-list'),
    path('rodzaje', views.RodzajeList.as_view(), name='rodzaje-list'),
    path('rodzaje/<int>:pk', views.RodzajeDetail.as_view(), name='rodzaje-details'),
    path('adopcja', views.AdopcjaList.as_view(), name='adopcja-list'),
    path('adopcja/<int:pk>', views.AdopcjaDetail.as_view(), name='adopcja-details'),
    path('zwierze', views.ZwierzeList.as_view(), name='zwierze-list'),
    path('zwierze/<int:pk>', views.ZwierzeDetail.as_view(), name='zwierze-details'),
    path('pracownik', views.PracownikList.as_view(), name='pracownik-list'),
    path('pracownik/<int:pk>', views.PracownikDetail.as_view(), name='pracownik-details'),
    path('zabieg', views.ZabiegiList.as_view(), name='zabieg-list'),
    path('zabieg/<int:pk>', views.ZabiegiDetail.as_view(), name='zabieg-details'),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]


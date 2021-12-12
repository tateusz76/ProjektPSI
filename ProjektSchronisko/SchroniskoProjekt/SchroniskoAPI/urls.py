from django.urls import path, include
from . import views

urlpatterns = [
    path('stanowisko', views.StanowiskoList.as_view(), name='stanowisko_list'),
    path('rodzaje', views.RodzajeList.as_view(), name='rodzaje_list'),
    path('adopcja', views.AdopcjaList.as_view(), name='adopcja_list'),
    path('adopcja/<int:pk>', views.AdopcjaDetail.as_view(), name='adopcja_detail'),
    path('zwierze', views.ZwierzeList.as_view(), name='zwierze_list'),
    path('zwierze/<int:pk>', views.ZwierzeDetail.as_view(), name='zwierze_details'),
    path('pracownik', views.PracownikList.as_view(), name='pracownik_list'),
    path('pracownik/<int:pk>', views.PracownikDetail.as_view(), name='pracownik_details'),
    path('zabieg', views.ZabiegiList.as_view(), name='zabieg_list'),
    path('zabieg/<int:pk>', views.ZabiegiDetail.as_view(), name='zabieg_details'),
]


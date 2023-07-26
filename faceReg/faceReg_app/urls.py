from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name ='reg-home'),
    path('media/', views.media, name = "reg-media"),
    path('radio/', views.radio, name = "reg-radio"),
]

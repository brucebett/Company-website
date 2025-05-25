from django.urls import path
from ym import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),

]

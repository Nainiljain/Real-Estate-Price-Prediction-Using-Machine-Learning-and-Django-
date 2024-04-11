from django.urls import path
from . import views

urlpatterns = [
    path('', views.rate_change, name='rate_change'),
]
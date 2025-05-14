from django.urls import path
from . import views

urlpatterns = [
    path('plot/', views.plot_view, name='plot'),
    path('', views.index, name='index'),
]
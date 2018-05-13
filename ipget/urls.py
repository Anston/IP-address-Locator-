from django.urls import path

from . import views

app_name = 'ipget'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='reset'),
    path('results/', views.results, name='results'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.home, name='home'),
    path('templates/review', views.review, name='review'),
    # path('templates/score', views.score, name='score'),
    # path('2/', views.2, name='2'),
    # path('3/', views.3, name='3'),

]
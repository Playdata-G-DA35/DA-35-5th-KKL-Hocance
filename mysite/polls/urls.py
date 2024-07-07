from django.urls import path
from . import views
from .views import *

app_name='polls' ##게시판 앱

urlpatterns = [
    path('', index),
    path('board/', board, name="board"),
    path('board/create', views.create),
    path('board/<int:pk>', views.read, name="read"),
    path('board/delete/<int:id>', views.delete),
]
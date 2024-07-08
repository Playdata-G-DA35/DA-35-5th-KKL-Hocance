from django.urls import path
from . import views
from .views import *

app_name='polls' ##게시판 앱

urlpatterns = [
    path('board/', views.board, name="board"),
    path('board/<int:pk>', views.read, name="read"),

]
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # 회원가입 URL 
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),# 로그인URL
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'), # 로그아웃URL
   
]
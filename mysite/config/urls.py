"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import home_view 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # 기본 홈 페이지
   

    # 각 폴더의 urls에서 url 따올수있도록 연결
    path('accounts/', include('accounts.urls')),   
    path('accounts/allauth/', include('allauth.urls')),  

    path('pages/', include('pages.urls')),
    path('polls/',include('polls.urls')),
    path('chart/', include('chart.urls')), # chart url 분리
    path('review_upload/', include(('review_upload.urls', 'review_upload'), namespace='review_upload')),
]

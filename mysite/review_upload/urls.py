# review_app/urls.py
# url 매핑 설정

from django.urls import path
from .views import upload_review, upload_success

app_name = 'review_upload'

urlpatterns = [
    path('upload/', upload_review, name='upload_review'),
    path('upload/success/', upload_success, name='upload_success'),
]
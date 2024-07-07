# review_app/models.py
# 리뷰 업로드
# 파일을 열고 리뷰를 저장할 모델 정의

from django.db import models

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    date = models.DateField()
    sentiment = models.CharField(max_length=10)  # '감정' 컬럼을 위한 필드

    def __str__(self):
        return self.review

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Post(models.Model):
    title = models.CharField('제목', max_length=50)
    contents = models.TextField()
    pub_date = models.DateTimeField('PUBLISH DATE', default=timezone.now)
    mod_date = models.DateTimeField('작성일', auto_now=True)
    rating = models.FloatField('별점',null=True, blank=True)  # 별점 필드 추가


    def __str__(self): #게시판에 제목
        return self.title
    
    def get_previous(self): #작성일
        return self.get_previous_by_mod_date()
    
    def get_next(self):
        return self.get_next_by_mod_date()
    
    class Meta:
            verbose_name='post'

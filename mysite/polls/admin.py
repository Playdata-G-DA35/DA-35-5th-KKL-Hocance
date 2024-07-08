from django.contrib import admin
from review_upload.models import Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk','date', 'review', 'rating','sentiment')
    list_filter = ('date',)
    search_fields = ('date','review','rating')


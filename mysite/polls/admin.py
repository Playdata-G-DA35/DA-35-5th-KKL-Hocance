from django.contrib import admin
from .models import Post
# Register your models here.



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'mod_date', 'rating')
    list_filter=('mod_date',)
    search_fields = ('title','content','subject')



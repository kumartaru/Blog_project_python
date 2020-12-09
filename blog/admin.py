from django.contrib import admin
from blog.models import post
# Register your models here.
@admin.register(post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']
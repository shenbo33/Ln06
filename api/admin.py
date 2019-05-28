from django.contrib import admin

# Register your models here.
from .models import User  # 记得导包


@admin.register(User)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # 在后台列表下显示的字段

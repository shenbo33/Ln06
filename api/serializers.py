from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User  # 指定的模型类
        fields = ('id', 'username', 'password', 'userType',)  # 需要序列化的属性

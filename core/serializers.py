from djoser.serializers import (UserCreateSerializer as BaseUserCreate )
from django.contrib.auth.models import User
from .models import Extension

class StudentsCreateSerializer(BaseUserCreate):
    class Meta(BaseUserCreate.Meta):
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

    def save(self, **kwargs):
        user = User.objects.create_user(**self.validated_data)
        extension = Extension.objects.create(user=user,is_student=True)
        return user


class TeachersCreateSerializer(BaseUserCreate):
    class Meta(BaseUserCreate.Meta):
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

    def save(self, **kwargs):
        user = User.objects.create_user(**self.validated_data)
        extension = Extension.objects.create(user=user, is_teacher=True)
        return user
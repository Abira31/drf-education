from rest_framework import serializers

from .models import (Teachers,Subjects,
                     Groups)

class TeachersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['first_name','last_name','url']

class SubjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['name','url']

class GroupsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['name','url']
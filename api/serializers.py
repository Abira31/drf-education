from rest_framework import serializers

from .models import Teachers

class TeachersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['first_name','last_name','url']
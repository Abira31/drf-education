from rest_framework.viewsets import ModelViewSet

from .serializers import TeachersSerializers

from .models import Teachers
class TeachersViewSet(ModelViewSet):
    serializer_class = TeachersSerializers
    queryset = Teachers.objects.all()
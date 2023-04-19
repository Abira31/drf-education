from rest_framework.viewsets import ModelViewSet

from .serializers import (TeachersSerializers,
                          SubjectsSerializers)

from .models import (Teachers,Subjects)
class TeachersViewSet(ModelViewSet):
    serializer_class = TeachersSerializers
    queryset = Teachers.objects.all()

class SubjectsViewSet(ModelViewSet):
    serializer_class = SubjectsSerializers
    queryset = Subjects.objects.all()
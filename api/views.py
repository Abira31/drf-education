from rest_framework.viewsets import ModelViewSet

from .serializers import (TeachersSerializers,
                          SubjectsSerializers,
                          GroupsSerializers)

from .models import (Teachers,Subjects,
                     Groups)
class TeachersViewSet(ModelViewSet):
    serializer_class = TeachersSerializers
    queryset = Teachers.objects.all()

class SubjectsViewSet(ModelViewSet):
    serializer_class = SubjectsSerializers
    queryset = Subjects.objects.all()

class GroupsViewSet(ModelViewSet):
    serializer_class = GroupsSerializers
    queryset = Groups.objects.all()
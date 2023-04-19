from rest_framework.viewsets import ModelViewSet

from .serializers import (TeachersSerializers,
                          SubjectsSerializers,
                          GroupsSerializers,
                          SubjectSerializers)

from .models import (Teachers,Subjects,
                     Groups,Subject)
class TeachersViewSet(ModelViewSet):
    serializer_class = TeachersSerializers
    queryset = Teachers.objects.all()

class SubjectsViewSet(ModelViewSet):
    serializer_class = SubjectsSerializers
    queryset = Subjects.objects.all()

class GroupsViewSet(ModelViewSet):
    serializer_class = GroupsSerializers
    queryset = Groups.objects.all()

class SubjectViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = SubjectSerializers
    queryset = Subject.objects\
        .select_related('subject')\
        .prefetch_related('group')\
        .prefetch_related('teacher')
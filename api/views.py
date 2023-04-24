from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Prefetch
from .serializers import (TeachersSerializers,
                          SubjectsSerializers,
                          GroupsSerializers,
                          StudentsSerializers,
                          StudentsDetailSerializers,
                          GroupDistributionSerializers,
                          SubjectSerializers,
                          TeacherDetailSerializers,
                          SubjectSaveSerializers)

from .models import (Teachers,Subjects,
                     Groups,Subject,
                     Students,Marks,
                     User)

from core.permissions import IsTeacherOrReadOnly,IsAdminUserOrReadOnly



class TeachersViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = TeachersSerializers
    queryset = Teachers.objects.all().select_related('teacher')
    def get_serializer_class(self):
        pk = self.kwargs.get('pk',None)
        if pk:
            return TeacherDetailSerializers
        return self.serializer_class


class SubjectsViewSet(ModelViewSet):
    serializer_class = SubjectsSerializers
    queryset = Subjects.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
#
class GroupsViewSet(ModelViewSet):
    serializer_class = GroupsSerializers
    queryset = Groups.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]

    def get_object_student(self,pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise ValidationError({"message_error": f"Student with this id = {pk}  does not exist"})
        except ValueError:
            raise ValidationError({"message_error": f"Student id must not be empty"})

    def get_object_group(self,pk):
        try:
            return Groups.objects.get(pk=pk)
        except Groups.DoesNotExist:
            raise ValidationError({"message_error": f"Group with this id = {pk}  does not exist"})
        except ValueError:
           raise ValidationError({"message_error": f"Group id must not be empty"})
    @action(detail=False, methods=['POST'],
            serializer_class=GroupDistributionSerializers)
    def group_to_a_student(self, request,pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    @action(detail=False,methods=['PUT'],
            serializer_class=GroupDistributionSerializers)
    def update_student_group(self,request):
        student = self.get_object_student(request.data.get('student_id'))
        group = self.get_object_group(request.data.get('group_id'))
        student.group = group
        student.save()
        return Response(status=status.HTTP_200_OK)

#
class SubjectViewSet(ModelViewSet):
    serializer_class = SubjectSerializers
    queryset = Subject.objects\
        .select_related('subject')\
        .prefetch_related('group')\
        .prefetch_related('teacher')
    permission_classes = [IsAdminUserOrReadOnly]
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubjectSerializers
        return SubjectSaveSerializers

    def create(self, request, *args, **kwargs):
        serializers = SubjectSaveSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = SubjectSaveSerializers(instance=instance,data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(status=status.HTTP_200_OK)

    def get_object(self):
        try:
            subject = Subject.objects.get(id=self.kwargs.get('pk'))
            return subject
        except Subject.DoesNotExist:
            raise ValidationError({"message_error": f"Subject with this id = {self.kwargs.get('pk')}  does not exist"})


class StudentsViewSet(ModelViewSet):
    def get_serializer_class(self):
        pk = self.kwargs.get('pk',None)
        if pk is not None:
            return StudentsDetailSerializers
        return StudentsSerializers
    def get_queryset(self):
        if self.kwargs.get('group_pk',None):
            return Students.objects.filter(group=self.kwargs['group_pk'])\
                .select_related('student')\
                .select_related('group')

        return Students.objects.all()\
            .select_related('student')\
            .prefetch_related('group',
                            Prefetch('marks',queryset=Marks.objects.all()\
                                     .select_related('subject')
                                     )
                            )
    def get_serializer_context(self):
        return {'group_pk': self.kwargs.get('group_pk',None),
                'request': self.request}

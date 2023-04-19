# from rest_framework.viewsets import ModelViewSet
# from rest_framework import generics
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import status
#
# from .serializers import (TeachersSerializers,
#                           SubjectsSerializers,
#                           GroupsSerializers,
#                           SubjectSerializers,
#                           StudentsSerializers,
#                           StudentsDetailSerializers)
#
# from .models import (Teachers,Subjects,
#                      Groups,Subject,
#                      Students)
# class TeachersViewSet(ModelViewSet):
#     serializer_class = TeachersSerializers
#     queryset = Teachers.objects.all()
#
# class SubjectsViewSet(ModelViewSet):
#     serializer_class = SubjectsSerializers
#     queryset = Subjects.objects.all()
#
# class GroupsViewSet(ModelViewSet):
#     serializer_class = GroupsSerializers
#     queryset = Groups.objects.all()
#
# class SubjectViewSet(ModelViewSet):
#     http_method_names = ['get']
#     serializer_class = SubjectSerializers
#     queryset = Subject.objects\
#         .select_related('subject')\
#         .prefetch_related('group')\
#         .prefetch_related('teacher')
#
# class StudentsViewSet(ModelViewSet):
#     def get_serializer_class(self):
#         pk = self.kwargs.get('pk',None)
#         if pk is not None:
#             return StudentsDetailSerializers
#         return StudentsSerializers
#     def get_queryset(self):
#         if self.kwargs.get('group_pk',None):
#             return Students.objects.filter(group=self.kwargs['group_pk']).select_related('group')
#
#         return Students.objects.select_related('group')
#     def get_serializer_context(self):
#         return {'group_pk': self.kwargs.get('group_pk',None),
#                 'request': self.request}

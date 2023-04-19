from rest_framework.viewsets import ModelViewSet
from .serializers import StudentsCreateSerializer,TeachersCreateSerializer
from django.contrib.auth.models import User

class StudentCreateAPIView(ModelViewSet):
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = StudentsCreateSerializer

class TeacherCreateAPIView(ModelViewSet):
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = TeachersCreateSerializer

from rest_framework import serializers

from .models import (Teachers,Subjects,
                     Groups,Subject,
                     Students)

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

class SubjectSerializers(serializers.ModelSerializer):
    subject = SubjectsSerializers()
    group = GroupsSerializers(many=True)
    teacher = TeachersSerializers(many=True)
    class Meta:
        model = Subject
        fields = ['subject','group','teacher']

class StudentsSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="students-detail")
    class Meta:
        model = Students
        fields = ['first_name','last_name','url']

class StudentsDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'




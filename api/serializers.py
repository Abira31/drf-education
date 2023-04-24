from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (Teachers,Subjects,
                     Groups,Subject,
                     Students,Marks)
from django.core.validators import MinValueValidator
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        read_only_fields = ['first_name','last_name','email']




class TeachersSerializers(serializers.ModelSerializer):
    teacher = UserSerializers()
    class Meta:
        model = Teachers
        fields = ['url','teacher']



class TeachersUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

#
class SubjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['name','url']
#
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

class TeacherSubjectSerializers(serializers.ModelSerializer):
    subject = SubjectsSerializers()
    group = GroupsSerializers(many=True)
    class Meta:
        model = Subject
        fields = ['subject', 'group']
class TeacherDetailSerializers(serializers.ModelSerializer):
    teacher = UserSerializers()
    subject = TeacherSubjectSerializers(many=True)
    class Meta:
        model = Teachers
        fields = ['teacher','subject']

class StudentsSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="students-detail")
    student = UserSerializers()
    group = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Students
        fields = ['url','student','group']
#
class MarksSerializers(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.name')
    class Meta:
        model = Marks
        fields = ['subject','date','mark']

class StudentsDetailSerializers(serializers.ModelSerializer):
    student = UserSerializers()
    marks = MarksSerializers(many=True)
    group = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Students
        fields = ['student','group','marks']

class GroupDistributionSerializers(serializers.Serializer):
    student_id = serializers.IntegerField(validators=[MinValueValidator(1)])
    group_id = serializers.IntegerField(validators=[MinValueValidator(1)])
    def save(self, **kwargs):
        student_id = self.validated_data['student_id']
        group_id = self.validated_data['group_id']
        try:
            student = Students.objects.get(id=student_id)
        except Students.DoesNotExist:
            raise serializers.ValidationError({"message_error":f"Student with this id = {student_id}  does not exist"})
        try:
            group = Groups.objects.get(id=group_id)
        except Groups.DoesNotExist:
            raise serializers.ValidationError({"message_error":f"Group with this id = {group_id}  does not exist"})

        student.group = group
        student.save()
        return student
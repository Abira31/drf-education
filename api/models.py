from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Subject(models.Model):
    subject = models.ForeignKey('Subjects',on_delete=models.CASCADE,blank=False,related_name='sub')
    group = models.ManyToManyField('Groups',related_name='subject',blank=True,null=True)
    teacher = models.ManyToManyField('Teachers',related_name='subject',blank=False)
    # def __str__(self):
    #     return f'{self.subject.name} группа - ' + ", ".join([a.name for a in self.group.all()])

class Groups(models.Model):
    name = models.CharField(max_length=120,blank=False)
    def __str__(self):
        return self.name

class Teachers(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(Groups,on_delete=models.CASCADE,blank=False)
    # def __str__(self):
    #     return f'{self.first_name}-{self.last_name} группа {self.group.name}'

class Subjects(models.Model):
    name = models.CharField(max_length=120, blank=False)
    # def __str__(self):
    #     return self.name

class Marks(models.Model):
    student = models.ForeignKey(Students,on_delete=models.CASCADE,blank=False,related_name='marks')
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE,blank=False)
    date = models.DateTimeField(auto_now_add=True)
    mark = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    # def __str__(self):
    #     return f'{self.student.last_name} предмет {self.subject.name} отценка: {self.mark} {self.date}'



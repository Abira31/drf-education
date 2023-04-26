from django.contrib.auth.models import User
from api.models import (Subject,Groups,
                        Teachers,Students,
                        Subjects,Marks)
from core.models import Extension
import random
teachers = [
    {'username': 'Антонин', 'password': 'T^5J+yHq2P', 'first_name': 'Антонин', 'last_name': 'Уваров',
     'email': 'fpoljakov@hotmail.com'},
    {'username': 'Марк', 'password': '&nym0vZzwX', 'first_name': 'Марк', 'last_name': 'Чернова',
     'email': 'alevtina_09@mail.ru'},
    {'username': 'Дементий', 'password': 'W*7EN7jnuj', 'first_name': 'Дементий', 'last_name': 'Белозерова',
     'email': 'savelevavalerija@hotmail.com'},
    {'username': 'Филарет', 'password': '&S7gIt3j8k', 'first_name': 'Филарет', 'last_name': 'Капустина',
     'email': 'alla2018@hotmail.com'},
    {'username': 'Ольга', 'password': 'lG)0D%yz!e', 'first_name': 'Ольга', 'last_name': 'Вишнякова',
     'email': 'komissarovsigizmund@rambler.ru'}
]
students = [
    {'username': 'Вера', 'password': '#eC3HVh8&2', 'first_name': 'Вера', 'last_name': 'Куликов',
     'email': 'pantelemon_52@gmail.com'},
    {'username': 'Болеслав', 'password': 'M&23NZQij3', 'first_name': 'Болеслав', 'last_name': 'Гришин',
     'email': 'anani1996@gmail.com'},
    {'username': 'Назар', 'password': 'z90IY$bd%s', 'first_name': 'Назар', 'last_name': 'Никифоров',
     'email': 'ustinovisa@rambler.ru'},
    {'username': 'Януарий', 'password': 'Jk5(06Ka$g', 'first_name': 'Януарий', 'last_name': 'Кулакова',
     'email': 'shilovaveronika@hotmail.com'},
    {'username': 'Яна', 'password': 'lRl%N24kO&', 'first_name': 'Яна', 'last_name': 'Панова',
     'email': 'forehov@rambler.ru'},
    {'username': 'Глеб', 'password': 't63IKZeC_m', 'first_name': 'Глеб', 'last_name': 'Дмитриева',
     'email': 'rodionovaksenija@mail.ru'},
    {'username': 'Поликарп', 'password': '5lZnwawt%Y', 'first_name': 'Поликарп', 'last_name': 'Белякова',
     'email': 'romanovaangelina@yahoo.com'},
    {'username': 'Всемил', 'password': '*a73SreY9O', 'first_name': 'Всемил', 'last_name': 'Фролова',
     'email': 'volkovaanastasija@hotmail.com'},
    {'username': 'Селиван', 'password': 'f%b1vVWt6#', 'first_name': 'Селиван', 'last_name': 'Маслов',
     'email': 'alina85@mail.ru'},
    {'username': 'Валентин', 'password': 'e1K(JUmd*F', 'first_name': 'Валентин', 'last_name': 'Нестерова',
     'email': 'longin2020@gmail.com'},
    {'username': 'Галина', 'password': '&R&Me!Mhp7', 'first_name': 'Галина', 'last_name': 'Смирнова',
     'email': 'spartakponomarev@gmail.com'},
    {'username': 'Флорентин', 'password': '(#80YOEx2B', 'first_name': 'Флорентин', 'last_name': 'Белозерова',
     'email': 'kir45@hotmail.com'},
    {'username': 'Лука', 'password': '$3Ds7qm78l', 'first_name': 'Лука', 'last_name': 'Беспалов',
     'email': 'avgust87@hotmail.com'},
    {'username': 'Будимир', 'password': 'q$6HvzMA%_', 'first_name': 'Будимир', 'last_name': 'Петров',
     'email': 'marina_2002@rambler.ru'},
    {'username': 'Ананий', 'password': '65ZTnnK1&1', 'first_name': 'Ананий', 'last_name': 'Овчинников',
     'email': 'rjurik_05@yandex.ru'},
    {'username': 'Панкрат', 'password': '#7#F(n(CbH', 'first_name': 'Панкрат', 'last_name': 'Лихачева',
     'email': 'bazhenkabanov@gmail.com'},
    {'username': 'Фадей', 'password': '+c#&O1Jf8', 'first_name': 'Фадей', 'last_name': 'Фокина',
     'email': 'averjan1999@hotmail.com'},
    {'username': 'Ангелина', 'password': 't*7SzYxoLJ', 'first_name': 'Ангелина', 'last_name': 'Данилов',
     'email': 'timofeevagalina@hotmail.com'},
    {'username': 'Милан', 'password': 'jk5R^G0P1(', 'first_name': 'Милан', 'last_name': 'Афанасьева',
     'email': 'mihalovrostislav@hotmail.com'},
    {'username': 'Измаил', 'password': 'H8HSnU*Y!4', 'first_name': 'Измаил', 'last_name': 'Кондратьев',
     'email': 'foti_1976@gmail.com'},
]
groups = [
    {"name":"1 курс"},
    {"name":"2 курс"},
    {"name":"3 курс"},
    {"name":"4 курс"},
]
subjects = [
    {"name": "Биология"},
    {"name": "История"},
    {"name": "Иностранный язык"},
    {"name": "Физкультура"},
    {"name": "Русский язык"},
    {"name": "Математика"},
]


class Create:
    teachers = []
    students = []
    groups = []
    subjects = []
    teachers_group = []
    students_group = []
    @classmethod
    def _create_teacher(cls):
        for teacher in teachers:
            user = User.objects.create_user(**teacher)
            Extension.objects.create(user=user, is_teacher=True)
            cls.teachers_group.append(Teachers.objects.create(teacher=user))
            cls.teachers.append(user)

    @classmethod
    def _create_student(cls):
        for student in students:
            user = User.objects.create_user(**student)
            Extension.objects.create(user=user, is_student=True)
            cls.students.append(user)

    @classmethod
    def _create_group(cls):
        for group in groups:
            cls.groups.append(Groups.objects.create(**group))

    @classmethod
    def _create_subjects(cls):
        for subject in subjects:
            cls.subjects.append(Subjects.objects.create(**subject))

    @classmethod
    def _create_students(cls):
        for student in cls.students:
            cls.students_group.append(Students.objects.create(student=student,group=random.choice(cls.groups)))
    @classmethod
    def _create_subject(cls):
        for _ in range(0,5):
            subject = random.choice(cls.subjects)
            groups = random.choices(cls.groups,k=random.randint(1,len(cls.groups)))
            teachers = random.choices(cls.teachers_group,k=random.randint(1,3))
            sub = Subject.objects.create(subject=subject)
            sub.group.add(*[group.id for group in groups])
            sub.teacher.add(*[teacher.id for teacher in teachers])
    @classmethod
    def _create_marks(cls):
        for _ in range(0,100):
            student = random.choice(cls.students_group)
            subject = random.choice(cls.subjects)
            Marks.objects.create(student=student,subject=subject,mark=random.randint(2,5))



    @classmethod
    def create(cls):
        cls._create_teacher()
        cls._create_student()
        cls._create_group()
        cls._create_subjects()
        cls._create_students()
        cls._create_subject()
        cls._create_marks()

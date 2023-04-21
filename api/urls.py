from rest_framework_nested import routers
from core.views import StudentCreateAPIView,TeacherCreateAPIView
from .views import (TeachersViewSet,
                    SubjectsViewSet,
                    GroupsViewSet,
                    StudentsViewSet,
                    SubjectViewSet)

router = routers.DefaultRouter()
router.register('create/student',StudentCreateAPIView,basename='create_student')
router.register('create/teacher',TeacherCreateAPIView,basename='create_teacher')

router.register('teachers',TeachersViewSet)
router.register('subjects',SubjectsViewSet)
router.register('groups',GroupsViewSet)
router.register('subject',SubjectViewSet)
router.register('students',StudentsViewSet,basename='students')

groups_router = routers.NestedSimpleRouter(router,'groups',lookup='group')
groups_router.register('students',StudentsViewSet,basename='group-students')

urlpatterns = router.urls + groups_router.urls
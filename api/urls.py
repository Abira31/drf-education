from rest_framework_nested import routers
from .views import (TeachersViewSet,
                    SubjectsViewSet,
                    GroupsViewSet,
                    SubjectViewSet)

router = routers.DefaultRouter()
router.register('teachers',TeachersViewSet)
router.register('subjects',SubjectsViewSet)
router.register('groups',GroupsViewSet)
router.register('subject',SubjectViewSet)

urlpatterns = router.urls
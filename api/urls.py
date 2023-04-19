from rest_framework_nested import routers
from .views import (TeachersViewSet,
                    SubjectsViewSet,
                    GroupsViewSet)

router = routers.DefaultRouter()
router.register('teachers',TeachersViewSet)
router.register('subjects',SubjectsViewSet)
router.register('groups',GroupsViewSet)


urlpatterns = router.urls
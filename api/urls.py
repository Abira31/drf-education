from rest_framework_nested import routers
from .views import (TeachersViewSet,
                    SubjectsViewSet)

router = routers.DefaultRouter()
router.register('teachers',TeachersViewSet)
router.register('subjects',SubjectsViewSet)


urlpatterns = router.urls
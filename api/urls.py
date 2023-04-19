from rest_framework_nested import routers
from .views import TeachersViewSet

router = routers.DefaultRouter()
router.register('teachers',TeachersViewSet)


urlpatterns = router.urls
from rest_framework import routers

from users.api.views import UserViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls

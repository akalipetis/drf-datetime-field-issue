from rest_framework import routers

from simple_app import views


router = routers.SimpleRouter()
router.register(r'simple_models', views.SimpleModelViewSet)
router.register(r'main_models', views.MainModelViewSet)
urlpatterns = router.urls
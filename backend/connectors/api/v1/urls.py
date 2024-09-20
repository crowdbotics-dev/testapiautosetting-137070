from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137070ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137070", Testconnectors137070ViewSet, basename="testconnectors137070"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]

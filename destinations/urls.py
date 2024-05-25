from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet

router = DefaultRouter()
router.register(r'destinations', DestinationViewSet, basename='destination')

urlpatterns = [
    path('api/', include(router.urls)),
]

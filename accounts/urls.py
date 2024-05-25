from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, incoming_data, get_destinations_by_account_id
from . import views

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('incoming_data/', incoming_data, name='incoming_data'),
    path('api/destinations/', views.DestinationViewSet.as_view({'get': 'list'}), name='destination-list'),
    path('accounts/<int:account_id>/destinations/', get_destinations_by_account_id, name='get_destinations_by_account_id'),
]

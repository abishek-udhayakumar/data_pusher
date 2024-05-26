from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, DestinationViewSet, get_destinations_for_account, incoming_data

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('account/<uuid:account_id>/destinations/', get_destinations_for_account, name='get_destinations_for_account'),
    path('server/incoming_data/', incoming_data, name='incoming_data'),
]

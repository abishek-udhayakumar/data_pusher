# Importing necessary modules
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, DestinationViewSet, get_destinations_for_account, incoming_data

# Creating a router for automatic URL routing
router = DefaultRouter()
# Registering viewsets for 'accounts' and 'destinations' with the router
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)

# Defining urlpatterns for URL configuration
urlpatterns = [
    # Including router URLs for 'accounts' and 'destinations'
    path('', include(router.urls)),
    # URL pattern to get destinations for a specific account by account ID
    path('account/<uuid:account_id>/destinations/', get_destinations_for_account, name='get_destinations_for_account'),
    # URL pattern for receiving incoming data
    path('server/incoming_data/', incoming_data, name='incoming_data'),
]

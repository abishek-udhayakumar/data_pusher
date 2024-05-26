# Importing necessary modules
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
import requests
import json

# ViewSet for handling CRUD operations on the Account model
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()  # Queryset to retrieve all Account objects
    serializer_class = AccountSerializer  # Serializer class for serializing Account objects

    # Custom destroy method to delete an Account object and its associated destinations
    def destroy(self, request, *args, **kwargs):
        account = self.get_object()  # Retrieve the Account object to be deleted
        account.destinations.all().delete()  # Delete all associated Destination objects
        return super().destroy(request, *args, **kwargs)  # Call the default destroy method

# ViewSet for handling CRUD operations on the Destination model
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()  # Queryset to retrieve all Destination objects
    serializer_class = DestinationSerializer  # Serializer class for serializing Destination objects

# API view to get destinations for a specific account
@api_view(['GET'])
def get_destinations_for_account(request, account_id):
    try:
        # Retrieve the Account object with the given account_id
        account = Account.objects.get(account_id=account_id)
        # Retrieve all destinations associated with the account
        destinations = account.destinations.all()
        # Serialize the destinations and return the response
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)
    except Account.DoesNotExist:
        # If the account does not exist, return a 404 Not Found response
        return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

# API view to handle incoming data
@api_view(['POST'])
def incoming_data(request):
    # Extract app_secret_token from request headers
    app_secret_token = request.headers.get('CL-X-TOKEN')
    if not app_secret_token:
        # If app_secret_token is not provided, return a 401 Unauthorized response
        return Response({"error": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        # Retrieve the Account object using the app_secret_token
        account = Account.objects.get(app_secret_token=app_secret_token)
    except Account.DoesNotExist:
        # If the account does not exist, return a 401 Unauthorized response
        return Response({"error": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        # Parse the request body as JSON data
        data = json.loads(request.body)
    except json.JSONDecodeError:
        # If the JSON data is invalid, return a 400 Bad Request response
        return Response({"error": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not isinstance(data, dict):
        # If the data is not a dictionary, return a 400 Bad Request response
        return Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Iterate over all destinations associated with the account
    for destination in account.destinations.all():
        headers = destination.headers  # Get destination headers
        method = destination.http_method  # Get HTTP method
        url = destination.url  # Get destination URL
        try:
            # Send the data to the destination using appropriate HTTP method
            if method == 'GET':
                response = requests.get(url, headers=headers, params=data)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data)
            response.raise_for_status()  # Raise an exception for non-2xx responses
        except requests.RequestException as e:
            # Log error if request fails
            print(f"Error sending data to {url}: {e}")
    
    # Return a success response
    return Response({"status": "success"})

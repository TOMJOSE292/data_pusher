
from rest_framework import viewsets
from .models import Destination, Account
from .serializers import DestinationSerializer, AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

@api_view(['GET'])
def get_destinations_by_account_id(request, account_id):
    try:
        account = Account.objects.get(pk=account_id)
    except Account.DoesNotExist:
        return Response({"detail": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
    
    destinations = account.account_destinations.all()
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def incoming_data(request):
    token = request.headers.get('CL-X-TOKEN')
    if not token:
        return Response({"detail": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        account = Account.objects.get(app_secret_token=token)
    except Account.DoesNotExist:
        return Response({"detail": "Invalid Token"}, status=status.HTTP_401_UNAUTHORIZED)

    data = request.data
    for destination in account.account_destinations.all():
        headers = destination.headers
        if destination.http_method.lower() == 'get':
            response = requests.get(destination.url, params=data, headers=headers)
        else:
            response = requests.request(destination.http_method, destination.url, json=data, headers=headers)
        if response.status_code not in range(200, 300):
            return Response({"detail": "Error sending data"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail": "Data sent successfully"}, status=status.HTTP_200_OK)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django Data Pusher App!")

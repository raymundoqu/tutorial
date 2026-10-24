from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

user = {
    "username": "raymundoqu",
    "name": "Raymundo Quintero",
    "email": "raymundoquintero@gmail.com",
    "birthday": "2007-11-28",
    "password": "123",
    "phone": "6679883821"
}
@api_view(['POST'])
def create_user(request):
    serialized_data = UserSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request):
    data = UserSerializer(data=request.data)
    birth = data['birth_day']
    return Response(data)

from users.models import User
    
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serialized_users = UserSerializer(users, many=True)
    return Response(serialized_users.data)
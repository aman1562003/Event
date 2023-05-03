from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializer import EventSerializer
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer




@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid username or password'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

    




@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create the new user
    user = User.objects.create(
        username=username,
        password=make_password(password),
        email=email,
    )

    # Return a success message
    return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)

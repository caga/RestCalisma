from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer,GroupSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endponit that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permisson_classes=[permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """API enpoint tahat allows groups to be viewed or edited.
    """
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    permisson_classes=[permissions.IsAuthenticated]



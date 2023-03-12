"""
Views for user Api
"""

from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create new user"""
    serializer_class = UserSerializer

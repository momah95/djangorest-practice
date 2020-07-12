from rest_framework import filters, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# from lib code
from . import models, serializers

# Create your views here.
class UserView(viewsets.ReadOnlyModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all().order_by("date_joined")

    # permission_classes = (IsAuthenticated,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email', 'last_name', 'first_name')
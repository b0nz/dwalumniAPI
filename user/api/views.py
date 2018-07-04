
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import detail_route, list_route
from django_filters.rest_framework import DjangoFilterBackend
import requests
from rest_framework_jwt.settings import api_settings
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action

from ..serializers import UserSerializer, ProfileSerializer
from ..models import Profile

class UserViewset(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    filter_fields = ('username', 'email',)
    search_fields = ('username', 'email',)
    ordering_fields = ('__all__')

    @detail_route(methods=['get'], permission_classes=[IsAuthenticated])
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(methods=['get'], permission_classes=[IsAuthenticated], detail=False)
    def get_schema(self, request):
        fields = User._meta.get_fields()
        field_names = [f.name for f in fields
            if not (f.is_relation)]

        return Response(
            field_names,
            status=status.HTTP_200_OK
        )

    @detail_route(methods=['get', 'post', 'patch'], permission_classes=[IsAuthenticated])
    def profile(self, request, pk=None):
        try:
            profile = Profile.objects.filter(user=pk)
        except Profile.DoesNotExist:
            return Response('not found')

        if request.method == 'GET':
            serializer = ProfileSerializer(profile, many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer = ProfileSerializer(profile)
            return Response(request.DATA)

class ProfileViewset(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
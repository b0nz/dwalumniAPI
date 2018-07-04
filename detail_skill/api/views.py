from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from ..models import DetailSkill, UserDetailSkill
from ..serializers import DetailSkillSerializer, UserDetailSkillSerializer


class DetailSkillViewset(viewsets.ModelViewSet):
    queryset = DetailSkill.objects.all()
    serializer_class = DetailSkillSerializer
    filter_backends = (
        SearchFilter,
    )
    filter_fields = ('name', 'skill',)
    search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserDetailSkillViewset(viewsets.ModelViewSet):
    queryset = UserDetailSkill.objects.all()
    serializer_class = UserDetailSkillSerializer
    # filter_backends = (
    #     SearchFilter,
    # )
    # filter_fields = ('name', 'skill',)
    # search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

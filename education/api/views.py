from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from ..models import Education, Major, UserEducation
from ..serializers import EducationSerializer, MajorSerializer, UserEducationSerializer


class UserEducationViewset(viewsets.ModelViewSet):
    queryset = UserEducation.objects.all()
    serializer_class = UserEducationSerializer
    filter_backends = (
        SearchFilter,
    )
    filter_fields = ('education','major', 'degree', 'begining_year', 'end_year',)
    search_fields = ('education',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EducationViewset(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    filter_backends = (
        SearchFilter,
    )
    filter_fields = ('name',)
    search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MajorViewset(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    filter_backends = (
        SearchFilter,
    )
    filter_fields = ('name',)
    search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

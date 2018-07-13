from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from ..models import Certificate
from ..serializers import CertificateSerializer


class CertificateViewset(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    #filter_backends = (
    #    SearchFilter,
    #)
    # filter_fields = ('',)
    # search_fields = ('title', 'desc',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def partial_update(self, request, pk=None, format='json'):
        instance = self.queryset.get(pk=pk)
        serializer = CertificateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            certificate = serializer.save(updated_by=request.user)
            if course:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors}, status=status.HTTP_403_FORBIDDEN)

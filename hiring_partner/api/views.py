from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from ..models import HiringPartner
from ..serializers import HiringPartnerSerializer


class HiringPartnerViewset(viewsets.ModelViewSet):
    queryset = HiringPartner.objects.all()
    serializer_class = HiringPartnerSerializer
    filter_backends = (
        SearchFilter,
    )
    filter_fields = ('company',)
    search_fields = ('company',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

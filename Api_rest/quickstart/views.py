
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AlimentosResSerializer, PlatosResSerializer
from .models import Alimento, Plato


class AlimentosResViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all().order_by('id')
    serializer_class = AlimentosResSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlatosResViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all().order_by('id')
    serializer_class = PlatosResSerializer
    permissions_classes = [permissions.IsAuthenticated]
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializers import AtracaoSerializer
from atracoes.models import Atracao


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nome', 'descricao')

    def list(self, request, *args, **kwargs):
        return super(AtracaoViewSet, self).list(request, *args, **kwargs)

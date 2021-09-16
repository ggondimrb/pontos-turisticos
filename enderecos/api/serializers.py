from enderecos.models import Endereco
from rest_framework.serializers import ModelSerializer


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['linha1', 'linha2', 'cidade',
                  'estado', 'pais', 'latitude', 'longitude']

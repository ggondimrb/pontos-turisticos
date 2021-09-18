from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import DocIdentificacao, PontoTuristico, Atracao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class DocIdentficacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    doc_identificacao = DocIdentficacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado',
                  'foto', 'atracoes', 'endereco', 'descricao_completa', 'doc_identificacao')

        #read_only_fields = ('comentarios, avaliacoes')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response


class PontoTuristicoViewsSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')
    lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset.filter(nome__iexact=nome)

        if descricao:
            queryset.filter(descricao__iexact=descricao)
        return queryset

# Aqui substituimos o metodo list do rest framework e podemos retornar qualquer  coisa.
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewsSet, self).list(request, *args, **kwargs)

# Aqui substituimos o metodo create do rest framework e podemos substituir por qualquer coisa.
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewsSet, self).create(request, *args, **kwargs)

# Delete é um otimo exemplo de substituição do existente no rest framework
# Aqui podemos apenas inativar um item ou gerar um log de quem está excluindo.
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewsSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewsSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewsSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewsSet, self).partial_update(request, *args, **kwargs)

# Para recurso especifico.
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass

from tastypie.resources import ModelResource
from evento.models import TipoInscricao


class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get']
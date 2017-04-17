from tastypie.resources import ModelResource
from tastypie import fields, utils
from evento.models import TipoInscricao, Inscricoes, PessoaFisica
from django.contrib.auth.models import User


class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get']


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']


class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get']


class InscricaoResource(ModelResource):
    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa')
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get']
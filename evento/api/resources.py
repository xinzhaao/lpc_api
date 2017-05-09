from tastypie.resources import ModelResource
from tastypie import fields, utils
from evento.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization




class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']

class PessoaResource(ModelResource):

    class Meta:
            queryset = Pessoa.objects.all()
            resource_name = 'pessoa'
            allowed_methods = ['get','post','put','delete']
            authorization = Authorization()



class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()

class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()


class EventoResource(ModelResource):
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = Evento.objects.all()
        resource_name = 'evento'
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()

class InscricaoResource(ModelResource):
    pessoafisica = fields.ToOneField(PessoaFisicaResource, 'pessoafisica')
    evento = fields.ToOneField(EventoResource, 'evento')
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()

class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class EventoCientificoResource(ModelResource):
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()


class ArtigoCientificoResource(ModelResource):
    evento = fields.ToOneField(EventoCientificoResource, 'evento')
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()




class ArtigoAutorResource(ModelResource):
    artigocientifico = fields.ToOneField(ArtigoCientificoResource, 'artigoCientifico')
    autor = fields.ToOneField(AutorResource, 'autor')
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()

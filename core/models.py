from django.db import models
from django.utils.translation import gettext_lazy as _
#Gera um código hexadecimal aleatorio
import uuid

from stdimage.models import StdImageField
# Create your models here.

#Função criada para gerar um nome de arquivo diferente para cada arquivo upado
def get_file_path(instance, filename):
    #pegando a extensão do arquivo
    ext = filename.split('.')[-1]
    #pegando o nome
    filename =  f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    #Auto now add, seta data automaticamente na Adição
    criado = models.DateField(_('Criação'), auto_now_add=True)
    #Auto now, atualiza no update
    modificado = models.DateField(_('Atualização'), auto_now=True)
    ativo = models.BooleanField(_('Ativo?'), default=True)
    class Meta:
        abstract = True


    
class Servico(Base):
    #Icones do template
    ICONE_CHOICES = {
        ('lni-cog', _('Engrenagem')),
        ('lni-stats-up', _('Design')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Camadas')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
    }
    servico = models.CharField(_('Serviço'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=200)
    #Fazendo um combo box com as opções de icones
    icone = models.CharField(_('Ícone'), max_length=12, choices=ICONE_CHOICES)


    class Meta:
        #Nome de apresentação da classe é o verbose_name
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    #Apresenta o objeto pelo nome dele
    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField(_('Cargo'), max_length=100)
    
    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField(_('Nome'), max_length=100)
    #Remoção em cascata caso o cargo não exista mais
    
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    #Lembrando que irá para o repositorio media do projeto
    #no parametro upload_to deve receber a função que gera o nome unico do arquivo
    imagem = StdImageField(_('Imagem'), upload_to= get_file_path, variations={'thumb':{'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram =  models.CharField('Instagram', max_length=100, default='#')
    twitter =  models.CharField('Twitter', max_length=100, default='#')

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')
    
    def __str__(self):
        return self.nome

class Feature(Base):

    ICONE_CHOICES = {
        ('lni-rocket',_('Foguete')),
        ('lni-laptop-phone',_('Laptop')),
        ('lni-cog',_('Engrenagem')),
        ('lni-leaf',_('Folha')),
        ('lni-layers',_('Camadas')),

    }
    titulo = models.CharField(_('Titulo'),max_length=100)
    icone = models.CharField(_('Ícone'),max_length=16,choices=ICONE_CHOICES)
    descricao = models.TextField(_('Descrição'),max_length=200)

    class Meta:
        verbose_name='Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.titulo

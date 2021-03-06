from django.db import models

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
    criado = models.DateField('Criação', auto_now_add=True)
    #Auto now, atualiza no update
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    class Meta:
        abstract = True


    
class Servico(Base):
    #Icones do template
    ICONE_CHOICES = {
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Design'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Camadas'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    }
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    #Fazendo um combo box com as opções de icones
    icone = models.CharField('Ícone', max_length=12, choices=ICONE_CHOICES)


    class Meta:
        #Nome de apresentação da classe é o verbose_name
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    #Apresenta o objeto pelo nome dele
    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    #Remoção em cascata caso o cargo não exista mais
    
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    #Lembrando que irá para o repositorio media do projeto
    #no parametro upload_to deve receber a função que gera o nome unico do arquivo
    imagem = StdImageField('Imagem', upload_to= get_file_path, variations={'thumb':{'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram =  models.CharField('Instagram', max_length=100, default='#')
    twitter =  models.CharField('Twitter', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
    
    def __str__(self):
        return self.nome

class Feature(Base):

    ICONE_CHOICES = {
        ('lni-rocket','Foguete'),
        ('lni-laptop-phone','Laptop'),
        ('lni-cog','Engrenagem'),
        ('lni-leaf','Folha'),
        ('lni-layers','Camadas'),

    }
    titulo = models.CharField('Titulo',max_length=100)
    icone = models.CharField('Ícone',max_length=16,choices=ICONE_CHOICES)
    descricao = models.TextField('Descrição',max_length=200)

    class Meta:
        verbose_name='Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.titulo

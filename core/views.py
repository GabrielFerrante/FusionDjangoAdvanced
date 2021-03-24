from django.shortcuts import render
from .models import Servico,Funcionario, Feature
from django.db.models import Q
from django.views.generic import FormView
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
#CLASS BASED VIEW
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        #ORDERNAR POR QUALQUER CAMPO 
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionario'] = Funcionario.objects.order_by('?').all()
        context['featureRight'] = Feature.objects.filter(id__lte=Feature.objects.count()/2)
        context['featureLeft'] = Feature.objects.filter(id__gt=Feature.objects.count()/2)
        return context
    

    def form_valid(self, form, *args, **kwargs):
        form.sendEmail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


#PARA MOSTRAR ERROS COMO 404 E 500, BASTA TER UM TEMPLATE COM O NOME DO ERRO
#class NotFoundView(TemplateView):
 #   template_name = '404.html'

#class ProcessErrorView(TemplateView):
 #   template_name = '500.html'
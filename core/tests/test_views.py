from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome':'Gabrie',
            'email': "xuxa@hotmail.com",
            'assunto' : "Assunto",
            'mensagem' : "Xuxa"
        }
        self.client = Client()
    
    def test_form_valid(self):

        request = self.client.post(reverse_lazy('index'), data=self.dados)
        #Usamos o 302 pois o form_valid está redirecionando
        self.assertEquals(request.status_code, 302)

    
    def test_form_invalid(self):
        dados = {
            'nome':'Nome',
            'email':'sss@gmail.com'
        }
        request = self.client.post(reverse_lazy('index'),data=dados)
        self.assertEquals(request.status_code, 200)
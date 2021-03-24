from django.test import TestCase
from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felicity Jones'
        self.email = 'fe@gmail.com'
        self.assunto = 'Assunto'
        self.mensagem = 'Mensagem'
        
        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem' : self.mensagem
        }
        self.form = ContatoForm(data=self.dados)


    def test_sendMail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.sendEmail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.sendEmail()

        self.assertEquals(res1, res2)
from django import forms

from django.core.mail.message import EmailMessage

#Tradução recomendada para forms
from django.utils.translation import gettext_lazy as _

class ContatoForm(forms.Form):
    nome = forms.CharField(label=_('Nome'),max_length=100)
    email = forms.EmailField(label=_('Email'), max_length=100)
    assunto = forms.CharField(label=_('Assunto'), max_length=100)
    mensagem = forms.CharField(label=_('Mensagem'), widget=forms.Textarea())

    def sendEmail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        n = _(nome)
        e = _(email)
        a = _(assunto)
        m = _(mensagem)


        conteudo = f'Nome: {n}\nEmail: {e}\nAssunto: {a}\nMensagem: {m}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br',],
            headers={'Reply-To':email}
        )
        mail.send()
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone')

    # é chamado antes de enviar o formulario pro db
    def clean(self):
        # cleaned_data = self.cleaned_data
        # erro nao deixa o formulario ser enviado
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='Invalid'
            )
        )
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='Invalid'
            )
        )

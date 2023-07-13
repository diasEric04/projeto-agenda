from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    # # (re)criando um campo (que ja existe)
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': 'Mudou'
    #         }
    #     ),
    #     label='primeiro nome',
    #     help_text='texto de ajuda'
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ATUALIZANDO UM WIDGET QUE TENHO NO CAMPO
        # campos que tenho
        # self.fields['first_name'].widget.attrs.update({
        #     'placeholder': 'Escreva aqui'
        # })
        # self.fields['first_name'].label = 'teste'
        self.fields['picture'].widget = forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )

    class Meta:
        model = Contact
        # campos que vao aparecer no form (que vem do model Contact)
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture'
        )
        # https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
        # CRIANDO UM WIDGET PRO CAMPO
        # widgets = {
        #     # nome do campo: 'widget que quero'
        #     'first_name': forms.TextInput(
        #         # atributos dentro da tag html
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui'
        #         }
        #     )
        # }

    # é chamado antes de enviar o formulario pro db
    # tem acesso a todos os campos
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                None,
                ValidationError(
                    'o campo First name e Last name mão pode ser iguais',
                    code='invalid'
                )
            )

        return super().clean()

    # clean_{nome_do_campo} é chamado automaticamente
    # e retorna o valor do campo
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            raise ValidationError('nao runfo')
        return first_name

from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


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
            },
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


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'já existe esse e-mail',
                    code='invalid'
                )
            )

        return email


class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Confirmação de senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            # cria senha no usuario de forma criptografada
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )
        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if email != current_email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        'já existe esse e-mail',
                        code='invalid'
                    )
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1

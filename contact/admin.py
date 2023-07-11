from django.contrib import admin
from . import models
# Register your models here.


# configuração do model na admin do django
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # a lista de campos que aparece na display da administração
    list_display = ('id', 'first_name', 'last_name')

    # lista em ordem das ordens de campos no display da adminsitração
    # se botar um '-' antes do nome, é por ordem decrescente, por padrao
    # é em ordem crescente
    ordering = ('id',)

    # cria uma aba de filtro com base no campo
    # list_filter = 'created_date'

    # cria um input search que pode pesquisar pelos campos abaixo
    search_fields = ('id', 'first_name', 'last_name')

    # numeros de campos por pagina (cria paginação)
    list_per_page = 1

    # tem um botao 'mostrar tudo' se for criado a paginação acima
    # e se não for posto um max, ele vai carregador todos os dados
    list_max_show_all = 200

    # os campos que podem ser editados os valores logo na lista,
    # sem que seja preciso entrar no campo em si
    # list_editable = ('first_name',)

    # os valores acima e abaixo pode entrar em conflito caso seja postos
    # nos dois

    # em qual campo seja posto o bolao de link que entra no campo
    list_display_links = ('id', 'first_name')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

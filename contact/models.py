from django.db import models
from django.utils import timezone

# Create your models here.

# id (primary key - automático) criado automaticamente pelo django
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)


# CRUD dos contatos da base de dados.
# sera necessario migration para base de dados
class Contact(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/

    # argumento: blank = True, poem o campo como opcional

    # arugmento: default = 'valor-default', cria um valor automatico que
    # nao precisa ser inserido na sua criação

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')

    # é o nome que sera usado la na administração do django para referencia
    # um dado na tabela
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
# depois é preciso registrar o model nos models da administração

# metodo save de Contact salva na base de dados os dados da instancia
# metodo delete de Contact deleta o contato da base de dados

# classmethod objects pode realizar alterações diretamente na db
#   get() # realiza uma consulta que deve retornar exatamente 1 dado
#       o parametro do get é a pesquisa (select * from ... where (PARAMETRO))
#   all() # retorna uma query set com TODOS
#   filter() # retorna um query set com varios dados com base na consulta
#   all().order_by() # ordena os dados com base no nome do campo passado
#       '-' significa decrescente

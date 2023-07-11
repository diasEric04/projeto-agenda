from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index')
]


# reconhece os arquivos estacios de static e media na BASE_DIR
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

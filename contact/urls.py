from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # contact (crud)
    path('contact/<int:contact_id>/details/', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),

    # user (crud)
    path('user/register/', views.register, name='user/register'),
    path('user/login/', views.login_view, name='user/login'),
    path('user/logout/', views.logout_view, name='user/logout'),
    path('user/update/', views.user_update, name='user/update'),
]


# reconhece os arquivos estacios de static e media na BASE_DIR
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

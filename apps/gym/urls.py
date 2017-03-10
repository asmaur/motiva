from django.conf.urls import url
from .views import *


#app_name = jobs

urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^aulas$', Aulas, name='aulas'),
    url(r'^treinadores$', Treinador, name='treinador'),
    url(r'^sobre$', Sobre, name='sobre'),
    url(r'^contato$', Contato, name='contato'),
    url(r'^programas$', Programas, name='programas'),
]
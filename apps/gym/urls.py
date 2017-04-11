from django.conf.urls import url, handler400, handler403, handler404, handler500
from .views import *


#app_name = jobs

urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^aulas$', Aulas, name='aulas'),
    url(r'^treinadores$', Treinador, name='treinador'),
    url(r'^sobre$', Sobre, name='sobre'),
    url(r'^contato/$', Contato, name='contato'),
    url(r'^programas$', Programas, name='programas'),
]

handler404 = 'apps.gym.views.custom_404'
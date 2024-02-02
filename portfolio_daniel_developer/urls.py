from django.contrib import admin
from django.urls import include, path
from .views import lista_proyectos, contactame, sobre_mi

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('proyectos/', lista_proyectos, name='lista_proyectos'),
    #path('', include('portfolio_daniel_dev.urls')),
    path('sobre_mi/', sobre_mi, name='sobre_mi'),
    path('contactame/', contactame, name='contactame')
    # Puedes agregar más URLs según tus necesidades
]

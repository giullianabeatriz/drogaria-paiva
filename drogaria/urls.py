from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('quemsomos/', views.quem_somos, name='quemsomos'),
    path('servicos/', views.servicos, name='servicos'),
    path('medicamentos/', views.medicamentos, name='medicamentos'),
]
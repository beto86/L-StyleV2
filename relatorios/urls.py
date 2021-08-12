from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RelatorioPorAlunoView

urlpatterns = [
    path('relatorio-aluno/<int:id>/',
         RelatorioPorAlunoView.as_view(), name='relatorio-aluno'),
]

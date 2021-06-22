from django.urls import path
from .views import EnderecoCreate, InstituicaoCreate, TurmaCreate
from .views import EnderecoUpdate, InstituicaoUpdate, TurmaUpdate
from .views import EnderecoDelete, InstituicaoDelete, TurmaDelete


urlpatterns = [
    path('cadastrar/endereco/', EnderecoCreate.as_view(),
         name='cadastrar-endereco'),
    path('cadastrar/instituicao/', InstituicaoCreate.as_view(),
         name='cadastrar-instituicao'),
    path('cadastrar/turma/', TurmaCreate.as_view(), name='cadastrar-turma'),

    path('editar/endereco/<int:pk>/',
         EnderecoUpdate.as_view(), name='editar-endereco'),
    path('editar/instituicao/<int:pk>/',
         InstituicaoUpdate.as_view(), name='editar-instituicao'),
    path('editar/turma/<int:pk>/',
         TurmaUpdate.as_view(), name='editar-turma'),

    path('excluir/endereco/<int:pk>/',
         EnderecoDelete.as_view(), name='excluir-endereco'),
    path('excluir/instituicao/<int:pk>/',
         InstituicaoDelete.as_view(), name='excluir-instituicao'),
    path('excluir/turma/<int:pk>/',
         TurmaDelete.as_view(), name='excluir-turma'),



]

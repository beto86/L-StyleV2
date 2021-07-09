from django.urls import path
from .views import InstituicaoCreate, TurmaCreate
from .views import InstituicaoUpdate, TurmaUpdate
from .views import InstituicaoDelete, TurmaDelete
from .views import InstituicaoList, TurmaList


urlpatterns = [
    path('cadastrar/instituicao/', InstituicaoCreate.as_view(),
         name='cadastrar-instituicao'),
    path('cadastrar/turma/', TurmaCreate.as_view(), name='cadastrar-turma'),

    path('editar/instituicao/<int:pk>/',
         InstituicaoUpdate.as_view(), name='editar-instituicao'),
    path('editar/turma/<int:pk>/',
         TurmaUpdate.as_view(), name='editar-turma'),

    path('excluir/instituicao/<int:pk>/',
         InstituicaoDelete.as_view(), name='excluir-instituicao'),
    path('excluir/turma/<int:pk>/',
         TurmaDelete.as_view(), name='excluir-turma'),

    path('listar/instituicoes', InstituicaoList.as_view(),
         name='listar-instituicoes'),
    path('listar/turmas', TurmaList.as_view(), name='listar-turmas'),



]

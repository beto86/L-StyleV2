from django.urls import path
from .views import InstituicaoCreate, TurmaCreate, CursoCreate
from .views import InstituicaoUpdate, TurmaUpdate, CursoUpdate
from .views import InstituicaoDelete, TurmaDelete, CursoDelete
from .views import InstituicaoList, TurmaList, CursoList


urlpatterns = [
    path('cadastrar/instituicao/', InstituicaoCreate.as_view(),
         name='cadastrar-instituicao'),
    path('cadastrar/turma/', TurmaCreate.as_view(), name='cadastrar-turma'),
    path('cadastrar/curso/', CursoCreate.as_view(), name='cadastrar-curso'),

    path('editar/instituicao/<int:pk>/',
         InstituicaoUpdate.as_view(), name='editar-instituicao'),
    path('editar/turma/<int:pk>/',
         TurmaUpdate.as_view(), name='editar-turma'),
    path('editar/curso/<int:pk>/',
         CursoUpdate.as_view(), name='editar-curso'),

    path('excluir/instituicao/<int:pk>/',
         InstituicaoDelete.as_view(), name='excluir-instituicao'),
    path('excluir/turma/<int:pk>/',
         TurmaDelete.as_view(), name='excluir-turma'),
    path('excluir/curso/<int:pk>/',
         CursoDelete.as_view(), name='excluir-curso'),

    path('listar/instituicoes', InstituicaoList.as_view(),
         name='listar-instituicoes'),
    path('listar/turmas', TurmaList.as_view(), name='listar-turmas'),
    path('listar/cursos', CursoList.as_view(), name='listar-cursos'),



]

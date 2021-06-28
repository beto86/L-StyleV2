from django.urls import path
from .views import QuestionarioCreate, QuestaoCreate, OpcaoCreate, TentativaCreate, TesteCreate
from .views import QuestionarioUpdate, QuestaoUpdate, OpcaoUpdate, TesteUpdate
from .views import QuestionarioDelete, QuestaoDelete, OpcaoDelete, TesteDelete
from .views import QuestionarioList, QuestaoList, OpcaoList, TentativaList, TesteList, RespostaList

urlpatterns = [
    path('cadastrar/questionario/', QuestionarioCreate.as_view(),
         name='cadastrar-questionario'),
    path('cadastrar/questao/', QuestaoCreate.as_view(),
         name='cadastrar-questao'),
    path('cadastrar/opcao/', OpcaoCreate.as_view(), name='cadastrar-opcao'),
    path('cadastrar/tentativa/', TentativaCreate.as_view(),
         name='cadastrar-tentativa'),
    path('cadastrar/teste/', TesteCreate.as_view(), name='cadastrar-teste'),

    path('editar/Questionario/<int:pk>/',
         QuestionarioUpdate.as_view(), name='editar-questionario'),
    path('editar/questao/<int:pk>/',
         QuestaoUpdate.as_view(), name='editar-questao'),
    path('editar/opcao/<int:pk>/',
         OpcaoUpdate.as_view(), name='editar-opcao'),
    path('editar/teste/<int:pk>/',
         TesteUpdate.as_view(), name='editar-teste'),

    path('excluir/questionario/<int:pk>/',
         QuestionarioDelete.as_view(), name='excluir-questionario'),
    path('excluir/questao/<int:pk>/',
         QuestaoDelete.as_view(), name='excluir-questao'),
    path('excluir/opcao/<int:pk>/',
         OpcaoDelete.as_view(), name='excluir-opcao'),
    path('excluir/teste/<int:pk>/',
         TesteDelete.as_view(), name='excluir-teste'),

    path('listar/questionarios', QuestionarioList.as_view(),
         name='listar-questionarios'),
    path('listar/questoes', QuestaoList.as_view(), name='listar-questoes'),
    path('listar/opcoes', OpcaoList.as_view(), name='listar-opcoes'),
    path('listar/tentativas', TentativaList.as_view(), name='listar-tentativas'),
    path('listar/testes', TesteList.as_view(), name='listar-testes'),
    path('listar/respostas', RespostaList.as_view(), name='listar-respostas'),


]

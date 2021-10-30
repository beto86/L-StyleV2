from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RelatorioPorAlunoView, RelatorioTurma, RelatorioCurso, PDFAlunoDetailView

urlpatterns = [
    path('relatorio/tentativa/<int:id>/',
         RelatorioPorAlunoView.as_view(), name='relatorio-aluno'),
    path('relatorio-turma/', RelatorioTurma.as_view(), name='relatorio-turma'),
    path('relatorio-curso/', RelatorioCurso.as_view(), name='relatorio-curso'),
    path('relatorios/tentativa/<int:id>/',
         PDFAlunoDetailView.as_view(), name='pdfAluno-detail'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RelatorioPorAlunoView, RelatorioTurma, PDFAlunoDetailView

urlpatterns = [
    path('relatorio/tentativa/<int:id>/',
         RelatorioPorAlunoView.as_view(), name='relatorio-aluno'),
    path('relatorios/', RelatorioTurma.as_view(), name='relatorios'),
    path('relatorios/tentativa/<int:id>/',
         PDFAlunoDetailView.as_view(), name='pdfAluno-detail'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PerfilUpdate, AlterarSenha, AlunoList, ProfessorList, AlunoCreate, ProfessorCreate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
    path('alterar-senha/', AlterarSenha.as_view(), name='alterar-senha'),
    path('listar-alunos/', AlunoList.as_view(), name='listar-alunos'),
    path('listar-professores/', ProfessorList.as_view(), name='listar-professores'),
    path('registrar-aluno/', AlunoCreate.as_view(), name='registrar-aluno'),
    path('registrar-professor/', ProfessorCreate.as_view(),
         name='registrar-professor'),
]

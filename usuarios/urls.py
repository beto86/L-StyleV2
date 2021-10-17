from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate, AlterarSenha, AlunoList, ProfessorList

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
    path('alterar-senha/', AlterarSenha.as_view(), name='alterar-senha'),
    path('listar-alunos/', AlunoList.as_view(), name='listar-alunos'),
    path('listar-professores/', ProfessorList.as_view(), name='listar-professores'),
]

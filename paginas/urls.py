from django.urls import path
from .views import IndexView, SobreView, QuemSomosView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('quem-somos/', QuemSomosView.as_view(), name='quem-somos'),
]

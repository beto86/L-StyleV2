from django.shortcuts import render
from django.views.generic import TemplateView
# import pandas as pd
from KolbStyleTeste.models import Resposta

# Create your views here.


def relatorio(request):
    # respostas = Resposta.objects.all().values()
    # df = pd.DataFrame(respostas)
    # df1 = df.head()
    # df2 = df[['id']]
    # dict = {
    #     "df2": df2.to_html(),
    #     "df1": df1.to_html()
    # }

    return render(request, "relatorio.html", context={})

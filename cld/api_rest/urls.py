from api_rest import views 
from django.urls import path


urlpatterns = [     
    path('estabelecimentos/', views.EstabelecimentoListServiceView.as_view(), name='estabelecimentos'),
    path('marcas/', views.MarcaListServiceView.as_view(), name='marcas'),
    path('unidades/', views.UnidadeListServiceView.as_view(), name='unidades'), 
    path('filtros/', views.FiltroListServiceView.as_view(), name='filtros'), 

    path('cadastrarEstabelecimento/', views.CadastrarEstabelecimentoServiceView.as_view(), name='cadastrarEstabelecimento'),
    path('cadastrarMarca/', views.CadastrarMarcaServiceView.as_view(), name='cadastrarMarca'),
    path('cadastrarUnidade/', views.CadastrarUnidadeServiceView.as_view(), name='cadastrarUnidade'),
    path('cadastrarFiltro/', views.CadastrarFiltroServiceView.as_view(), name='cadastrarFiltro'),

    path('atualizarEstabelecimento/', views.AtualizarEstabelecimentoServiceView.as_view(), name='atualizarEstabelecimento'), 
    path('atualizarMarca/', views.AtualizarMarcaServiceView.as_view(), name='atualizarMarca'),
    path('atualizarUnidade/', views.AtualizarUnidadeServiceView.as_view(), name=''),
    path('atualizarFiltro/', views.AtualizarFiltroServiceView.as_view(), name='atualizarFiltro'),

    path('excluirEstabelecimento/', views.ExcluirEstabelecimentoServiceView.as_view(), name='excluirEstabelecimento'),
    path('excluirMarca/', views.ExcluirMarcaServiceView.as_view(), name='excluirMarca'),
    path('excluirUnidade/', views.ExcluirUnidadeServiceView.as_view(), name='excluirUnidade'),
    path('excluirFiltro/', views.ExcluirFiltroServiceView.as_view(), name='excluirFiltro'),
]

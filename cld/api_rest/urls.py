from api_rest import views 
from django.urls import path


urlpatterns = [     
    path('estabelecimentos/', views.EstabelecimentoListServiceView.as_view(), name='estabelecimentos'),
    path('marcas/', views.MarcaListServiceView.as_view(), name='marcas'),
    path('unidades/', views.UnidadeListServiceView.as_view(), name='unidades'), 
    path('filtros/', views.FiltroListServiceView.as_view(), name='filtros'), 
    path('cestas/', views.CestaListServiceView.as_view(), name='cestas'),
    path('itens/', views.ItemCestaListServiceView.as_view(), name='itens'),

    path('cadastrarEstabelecimento/', views.CadastrarEstabelecimentoServiceView.as_view(), name='cadastrarEstabelecimento'),
    path('cadastrarMarca/', views.CadastrarMarcaServiceView.as_view(), name='cadastrarMarca'),
    path('cadastrarUnidade/', views.CadastrarUnidadeServiceView.as_view(), name='cadastrarUnidade'),
    path('cadastrarFiltro/', views.CadastrarFiltroServiceView.as_view(), name='cadastrarFiltro'),
    path('cadastrarCesta/', views.CadastrarCestaServiceView.as_view(), name='cadastrarCesta'),
    path('cadastrarItem/', views.CadastrarItemServiceView.as_view(), name='cadastrarItem'),

    path('atualizarEstabelecimento/', views.AtualizarEstabelecimentoServiceView.as_view(), name='atualizarEstabelecimento'), 
    path('atualizarMarca/', views.AtualizarMarcaServiceView.as_view(), name='atualizarMarca'),
    path('atualizarUnidade/', views.AtualizarUnidadeServiceView.as_view(), name=''),
    path('atualizarFiltro/', views.AtualizarFiltroServiceView.as_view(), name='atualizarFiltro'),
    path('atualizarCesta/', views.AtualizarCestaServiceView.as_view(), name='atualizarCesta'),
    path('atualizarItem/', views.AtualizarItemServiceView.as_view(), name='atualizarItem'),

    path('excluirEstabelecimento/', views.ExcluirEstabelecimentoServiceView.as_view(), name='excluirEstabelecimento'),
    path('excluirMarca/', views.ExcluirMarcaServiceView.as_view(), name='excluirMarca'),
    path('excluirUnidade/', views.ExcluirUnidadeServiceView.as_view(), name='excluirUnidade'),
    path('excluirFiltro/', views.ExcluirFiltroServiceView.as_view(), name='excluirFiltro'),
    path('excluirCesta/', views.ExcluirCestaServiceView.as_view(), name='excluirCesta'),
    path('excluirItem/', views.ExcluirItemServiceView.as_view(), name='excluirItem'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),  # Página inicial do app: lista de produtos
    path('novo/', views.criar_produto, name='criar_produto'),  # Página de criação de novo produto
    path('<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),  # Página de detalhes do produto
    path('<int:produto_id>/editar/', views.editar_produto, name='editar_produto'),
    path('<int:produto_id>/deletar/', views.deletar_produto, name='deletar_produto'),
]

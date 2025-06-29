from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()  # Busca todos os produtos no banco de dados
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

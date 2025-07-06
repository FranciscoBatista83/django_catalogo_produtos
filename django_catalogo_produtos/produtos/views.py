from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def lista_produtos(request):
    produtos = Produto.objects.all()  # Busca todos os produtos no banco de dados
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Verifica qual botão foi clicado
            if 'salvar_continuar' in request.POST:
                # Redireciona para a própria página de cadastro (formulário limpo)
                return redirect('criar_produto')
            else:
                # Redireciona para a lista de produtos
                return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    
    return render(request, 'produtos/criar_produto.html', {'form': form})

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})
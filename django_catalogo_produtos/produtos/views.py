from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm, CategoriaForm

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

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('detalhe_produto', produto_id=produto.id)
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto': produto})

def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')

    return render(request, 'produtos/deletar_produto.html', {'produto': produto})

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  # redireciona para a lista de produtos
    else:
        form = CategoriaForm()

    return render(request, 'produtos/criar_categoria.html', {'form': form})
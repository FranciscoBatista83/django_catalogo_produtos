from django import forms
from .models import Produto, Categoria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'categoria']

class CategoriaForm(forms.ModelForm):
     class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
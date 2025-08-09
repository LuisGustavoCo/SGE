from django import forms
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'selling_price']
        # Passando a estilização Bootstrap por aqui e repassando para o html por {{forms.as_p}}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),

        }
        # "Mudando" o nome no html
        labels = {
            'title': 'Título',
            'category': 'Categoria',
            'brand': 'Marca',
            'description': 'Descrição',
            'serie_number': 'Número de Série',
            'cost_price': 'Custo',
            'selling_price': 'Preço de Venda',
        }
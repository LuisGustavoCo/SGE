from django import forms
from . import models


class InflowForm(forms.ModelForm):

    class Meta:
        model = models.Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        # Passando a estilização Bootstrap por aqui e repassando para o html por {{forms.as_p}}
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}), 
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        # "Mudando" o nome no html
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição'
        }
from django import forms
from . import models


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = ['name', 'description']
        # Passando a estilização Bootstrap por aqui e repassando para o html por {{forms.as_p}}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), 
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        # "Mudando" o nome no html
        labels = {
            'name': 'Nome',
            'description': 'Descrição'
        }
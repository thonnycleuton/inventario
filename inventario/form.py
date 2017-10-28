from django import forms

from inventario.models import Colaborador, Produto, Setor


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Colaborador
        fields = ['username', 'first_name', 'last_name', 'email','data_nascimento', 'setor', 'telefone', 'foto',]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'setor': forms.Select(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'phone form-control'}),
            'foto': forms.FileInput(attrs={'class': 'btn-primary'}),
        }


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'patrimonio': forms.TextInput(attrs={'class': 'form-control'}),
            'nota_fiscal': forms.TextInput(attrs={'class': 'form-control'}),
            'colaborador': forms.Select(attrs={'class': 'form-control'}),
        }


class SetorForm(forms.ModelForm):

    class Meta:
        model = Setor
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),

        }

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from inventario.form import ProfileForm, ProdutoForm, SetorForm
from inventario.models import Produto, Setor, Colaborador


class ListProduto(ListView):
    model = Produto


class CreateProduto(CreateView):
    model = Produto
    success_url = reverse_lazy('inventario:produto_list')
    form_class = ProdutoForm

    def form_valid(self, form):
        form.save()
        return super(CreateProduto, self).form_valid(form)


class UpdateProduto(UpdateView):
    model = Produto
    success_url = reverse_lazy('inventario:produto_list')
    form_class = ProdutoForm

    def form_valid(self, form):
        form.save()
        return super(UpdateProduto, self).form_valid(form)


class DeleteProduto(DeleteView):
    model = Produto
    success_url = reverse_lazy('inventario:produto_list')


# Classe de View para Colaborador
class ListColaborador(ListView):
    model = Colaborador


class CreateColaborador(CreateView):
    model = Colaborador
    success_url = reverse_lazy('inventario:colaborador_list')
    form_class = ProfileForm

    def form_valid(self, form):
        form.save()
        return super(CreateColaborador, self).form_valid(form)


class UpdateColaborador(UpdateView):
    model = Colaborador
    success_url = reverse_lazy('inventario:colaborador_list')
    form_class = ProfileForm

    def form_valid(self, form):
        form.save()
        return super(UpdateColaborador, self).form_valid(form)


class DeleteColaborador(DeleteView):
    model = Colaborador
    success_url = reverse_lazy('inventario:colaborador_list')


# Comeca classes de view para Setores
class ListSetor(ListView):
    model = Setor


class CreateSetor(CreateView):
    model = Setor
    success_url = reverse_lazy('inventario:setor_list')
    form_class = SetorForm

    def form_valid(self, form):
        form.save()
        return super(CreateSetor, self).form_valid(form)


class UpdateSetor(UpdateView):
    model = Produto
    success_url = reverse_lazy('inventario:setor_list')
    form_class = SetorForm

    def form_valid(self, form):
        form.save()
        return super(UpdateSetor, self).form_valid(form)


class DeleteSetor(DeleteView):
    model = Setor
    success_url = reverse_lazy('inventario:setor_list')

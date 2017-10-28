from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from inventario.form import ProfileForm, ProdutoForm, SetorForm
from inventario.models import Produto, Setor, Colaborador


class ListProduto(ListView):
    model = Produto
    template_name = 'inventario/produto/produto_list.html'


class CreateProduto(CreateView):
    model = Produto
    success_url = reverse_lazy('inventario:produto_list')
    form_class = ProdutoForm
    template_name = 'inventario/produto/produto_form.html'

    def form_valid(self, form):
        form.save()
        return super(CreateProduto, self).form_valid(form)


class UpdateProduto(UpdateView):
    model = Produto
    success_url = reverse_lazy('inventario:produto_list')
    template_name = 'inventario/produto/produto_form.html'
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
    template_name = 'inventario/colaborador/colaborador_list.html'


class CreateColaborador(CreateView):
    model = Colaborador
    success_url = reverse_lazy('inventario:colaborador_list')
    template_name = 'inventario/colaborador/colaborador_form.html'
    form_class = ProfileForm

    def form_valid(self, form):
        form.save()
        return super(CreateColaborador, self).form_valid(form)


class UpdateColaborador(UpdateView):
    model = Colaborador
    success_url = reverse_lazy('inventario:colaborador_list')
    form_class = ProfileForm
    template_name = 'inventario/colaborador/colaborador_form.html'

    def form_valid(self, form):
        form.save()
        return super(UpdateColaborador, self).form_valid(form)


class DeleteColaborador(DeleteView):
    model = Colaborador
    success_url = reverse_lazy('inventario:colaborador_list')


def colaborador_delete(request, pk):

    colaborador = get_object_or_404(Setor, pk=pk)
    data = dict()
    if request.method == 'POST':
        colaborador.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        colaboradores = Colaborador.objects.all()
        data['html_list'] = render_to_string('inventario/colaborador/includes/partial_list.html', {
            'colaborador_list': colaboradores
        })
    else:
        context = {'colaborador': colaborador}
        data['html_form'] = render_to_string('inventario/colaborador/includes/partial_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


# Comeca classes de view para Setores
class ListSetor(ListView):
    model = Setor
    template_name = 'inventario/setor/setor_list.html'


class CreateSetor(CreateView):
    model = Setor
    success_url = reverse_lazy('inventario:setor_list')
    form_class = SetorForm
    template_name = 'inventario/setor/setor_form.html'

    def form_valid(self, form):
        form.save()
        return super(CreateSetor, self).form_valid(form)


class UpdateSetor(UpdateView):
    model = Produto
    success_url = reverse_lazy('inventario:setor_list')
    form_class = SetorForm
    template_name = 'inventario/setor/setor_form.html'

    def form_valid(self, form):
        form.save()
        return super(UpdateSetor, self).form_valid(form)


class DeleteSetor(DeleteView):
    model = Setor
    success_url = reverse_lazy('inventario:setor_list')


def setor_delete(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    data = dict()
    if request.method == 'POST':
        setor.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        setores = Setor.objects.all()
        data['html_list'] = render_to_string('inventario/setor/includes/partial_list.html', {
            'setor_list': setores
        })
    else:
        context = {'setor': setor}
        data['html_form'] = render_to_string('inventario/setor/includes/partial_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)

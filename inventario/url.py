from django.conf.urls import url

from inventario.views import ListProduto, CreateProduto, UpdateProduto, DeleteProduto, \
    ListColaborador, CreateColaborador, UpdateColaborador, DeleteColaborador, \
    ListSetor, CreateSetor, UpdateSetor, DeleteSetor

urlpatterns = [
    url(r'^$', ListProduto.as_view(), name='produto_list'),
    url(r'^produto-add/$', CreateProduto.as_view(), name='produto_add'),
    url(r'^produto-edit/(?P<pk>\d+)/$', UpdateProduto.as_view(), name='produto_edit'),
    url(r'^produto-delete/(?P<pk>\d+)/$', DeleteProduto.as_view(), name='produto_delete'),

    url(r'^colaborador/$', ListColaborador.as_view(), name='colaborador_list'),
    url(r'^colaborador-add/$', CreateColaborador.as_view(), name='colaborador_add'),
    url(r'^colaborador-edit/(?P<pk>\d+)/$', UpdateColaborador.as_view(), name='colaborador_edit'),
    url(r'^colaborador-delete/(?P<pk>\d+)/$', DeleteColaborador.as_view(), name='colaborador_delete'),

    url(r'^setor/$', ListSetor.as_view(), name='setor_list'),
    url(r'^setor-add/$', CreateSetor.as_view(), name='setor_add'),
    url(r'^setor-edit/(?P<pk>\d+)/$', UpdateSetor.as_view(), name='setor_edit'),
    url(r'^setor-delete/(?P<pk>\d+)/$', DeleteSetor.as_view(), name='setor_delete'),
]

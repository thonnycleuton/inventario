from django.contrib import admin

# Register your models here.
from inventario.models import Produto, Colaborador, Setor

admin.site.register(Produto)
admin.site.register(Colaborador)
admin.site.register(Setor)
from django.contrib import admin
from .models import ModelBorrar

@admin.register(ModelBorrar)
class AdminModelBorrar(admin.ModelAdmin):
    pass
    # list_display = ('nombre','detalle')
    search_fields = ['demo']
    # inlines = [ProfesionalHorarioInline]

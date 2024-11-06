from django.contrib import admin
from .models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug', 'autor', 'criado', 'status']
    prepopulated_fields = {'slug': ('titulo',)}
    list_filter = ['autor', 'status', 'criado']
    list_editable = ['status']
    search_fields = ['titulo', 'texto']
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    ordering = ['status', '-publicado']

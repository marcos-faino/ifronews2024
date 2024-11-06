from django.shortcuts import render
from django.views.generic import TemplateView

from news.models import New


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['news'] = New.objects.filter(status='publicado').all()
        return contexto

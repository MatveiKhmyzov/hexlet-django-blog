from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


# def index(request):
#     return redirect('article', 'python', 42)


def about(request):
    return render(request, 'about.html')

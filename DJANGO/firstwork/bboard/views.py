from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Bd, Rubric

# ВЫВОД ТЕКСТА
# def index(request):c
#     s = 'Список объявлений\n\n\n'
#     for bb in Bd.objects.order_by('-published'):
#         s += bb.title + '\n' + bb.content + '\n\n\n'
#     return HttpResponse(s, content_type='text/lain; charset=utf-8')


def index(request):
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    # return HttpResponse(bbs)
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bd.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    return render(request, 'bboard/by_rubric.html', context)


from django.views.generic.edit import CreateView
from .forms import BdForm

class BdCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BdForm
    success_url = reverse_lazy('index')         #'/bboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context




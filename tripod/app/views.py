from django.http import HttpResponse
from .models import Experiment, Config
from django.shortcuts import render, get_object_or_404

def index(request):
    experiments_list = Experiment.objects.order_by('-pub_date')
    context = {'experiments_list': experiments_list}
    return render(request, 'app/index.html', context)


def exp(request, experiment_id):
    experiment = get_object_or_404(Experiment, pk=experiment_id)
    context = {'experiment': experiment}
    return render(request, 'app/exp.html', context)


def config(request, config_id):
    config = get_object_or_404(Config, pk=config_id)
    context = {'config': config}
    return render(request, 'app/config.html', context)
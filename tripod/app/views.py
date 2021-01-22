from django.http import HttpResponse, HttpResponseRedirect
from .models import Experiment, Config, ExperimentForm, ConfigForm
from django.shortcuts import render, get_object_or_404
from .utils import check_settings

def index(request):
    experiments_list = Experiment.objects.order_by('-pub_date')
    context = {'experiments_list': experiments_list}
    return render(request, 'app/index.html', context)


def exp(request, experiment_id):
    experiment = get_object_or_404(Experiment, pk=experiment_id)
    context = {'experiment': experiment}
    return render(request, 'app/exp.html', context)


def addexp(request):

    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():

            # flag, error = check_settings(form.cleaned_data['settings'])
            # if flag:
            form.save()
            return HttpResponseRedirect('/app/')

    else:
        form = ExperimentForm()

    context = {'form': form}

    return render(request, 'app/addexp.html', context)


def config(request, config_id):
    config = get_object_or_404(Config, pk=config_id)
    context = {'config': config}
    return render(request, 'app/config.html', context)
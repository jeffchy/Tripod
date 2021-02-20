from django.http import HttpResponse, HttpResponseRedirect
from .models import Experiment, Config, ExperimentForm, ConfigForm
from django.shortcuts import render, get_object_or_404
from .core.default import Nodes, GPUs
from .core.checker import check_config_settings, check_experiment_settings

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

    if request.method == 'POST':



        print(request.POST)
        context = {
                    'config': config,
                    'scripts': '1',
                    'error': '2',
                    'nodes': Nodes,
                    'gpus': GPUs,
                   }
        return render(request, 'app/config.html', context)

    else:
        context = {
                    'config': config,
                    'nodes': Nodes,
                    'gpus': GPUs,
                   }
        return render(request, 'app/config.html', context)


def addconfig(request, experiment_id):
    experiment = get_object_or_404(Experiment, pk=experiment_id)
    error = ''

    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            add_exp_id = form.cleaned_data['experiment'].id

            settings = form.cleaned_data['config_settings']
            error += check_config_settings(settings)
            print(settings, error)
            if error:
                context = {'form': form, 'experiment': experiment, 'error': error}
                return render(request, 'app/addconfig.html', context)
            else:
                form.save()

                return HttpResponseRedirect('/app/exp/{}'.format(add_exp_id))
        else:
            error += "Invalid Form"

    else:
        form = ConfigForm()

    context = {'form': form, 'experiment': experiment, 'error': error}

    return render(request, 'app/addconfig.html', context)

from django.db import models
from django.forms import ModelForm
from django.forms import widgets
import datetime


class Experiment(models.Model):
    experiment_name = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published', default=datetime.date.today)
    settings = models.TextField()

    def __str__(self):
        return self.experiment_name


class Config(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    config_name = models.CharField(max_length=200, unique=True)
    config_settings = models.TextField()
    pub_date = models.DateTimeField('date published', default=datetime.date.today)

    def __str__(self):
        return self.config_name


class ExperimentForm(ModelForm):
    class Meta:
        model = Experiment
        fields = ['experiment_name', 'settings']
        widgets = {
            'experiment_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'settings': widgets.Textarea(attrs={'class': 'form-control'}),

        }


class ConfigForm(ModelForm):
    class Meta:
        model = Config
        fields = ['experiment', 'config_name', 'config_settings']
        widgets = {
            'experiment': widgets.Select(attrs={'class': 'form-control'}),
            'config_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'config_settings': widgets.Textarea(attrs={'class': 'form-control'}),
        }

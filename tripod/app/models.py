from django.db import models


class Experiment(models.Model):
    experiment_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    settings = models.TextField()

    def __str__(self):
        return self.experiment_name

class Config(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    config_name = models.CharField(max_length=200)
    config_settings = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.config_name
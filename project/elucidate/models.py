from django.db import models


class Sentence(models.Model):
    sentence = models.CharField(max_length=140)

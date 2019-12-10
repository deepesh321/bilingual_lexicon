from django.db import models
from django.utils import timezone

class Corpora(models.Model):
    lang1 = models.FileField(upload_to ='media/')
    lang2 = models.FileField(upload_to ='media/')
    created_date = models.DateTimeField(default=timezone.now)


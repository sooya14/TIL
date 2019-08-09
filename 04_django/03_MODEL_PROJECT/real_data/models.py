from django.db import models

class HotIssue(models.Model):
    data = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    rank = models.IntegerField()
    keyword = models.CharField(max_length=10)

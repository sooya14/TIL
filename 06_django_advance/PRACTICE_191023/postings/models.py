from django.db import models
from django.urls import reverse

# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length= 20)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("postings:postings_detail", kwargs={"postings_id": self.pk})

class Comment(models.Model):
    content = models.TextField()
    comment = models.ForeignKey(Posting, on_delete=models.CASCADE)
    
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    likes = models.DecimalField(max_digits=1000, decimal_places=3)
    text = models.TextField(default='patata')
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        # return f'{self.id}'
        return reverse("article-detail", kwargs={"my_id": self.id})

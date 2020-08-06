from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=3)
    sumary = models.TextField(default='patata')
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        # return f"/products/{self.id}/"
        return reverse("products:product_det", kwargs={"id": self.id})

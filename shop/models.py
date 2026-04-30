from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.URLField(max_length=500, blank=True)  #we use a link for now to make it easy
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.URLField()
    rating_rate = models.FloatField()
    rating_count = models.IntegerField()

    def __str__(self):
        return self.title
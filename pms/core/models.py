from django.db import models
from django.core.urlresolvers import reverse


# class User(models.Model):
#     firstname = models.CharField(max_length=40)
#     lastname = models.CharField(max_length=40)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.firstname


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('core:category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('core:product', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

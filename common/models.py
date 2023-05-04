from django.db import models
from django.core.exceptions import ValidationError
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Category(models.Model):
    title = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField(default=1)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.id == self.parent_id:
            raise ValidationError('Category parent id must be differnet')
        return super().clean()

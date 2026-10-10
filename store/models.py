from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='Products'
    )

    name = models.CharField(max_length=200)

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.CharField(
        max_length=300,
        blank=True
    )

    def __str__(self):
        return self.name
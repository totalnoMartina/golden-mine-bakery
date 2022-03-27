from django.db import models


class Category(models.Model):
    """ Categories of a product """
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)


    def __str__(self):
        """ A method to show name """
        return self.name


    def get_friendly_name(self):
        """ A method to show a friendly name """
        return self.friendly_name


class Product(models.Model):
    """ A model for a product """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """ A method to show name """
        return self.name

from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=20)
    units = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    quantity = models.IntegerField(default=0)
    date_of_last_delivery = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["name","quantity"]

    def __str__(self):
        return "{},{}".format(self.id,self.name)

    #def get_absolute_url(self):
        #"""
        #Returns the url to access a particular instance of the model.
        #"""
        #return reverse('model-detail-view', args=[str(self.id)])

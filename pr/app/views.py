from django.shortcuts import render


from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product



class ProductListView(generic.ListView):
    model = Product
    template_name = 'app/home.html'
    #form1 = Search()


    #def get_queryset(self):
    #    return Product.objects.filter(quantity__lte)
    #paginate_by = 2
     # о умолчанию файл будет называться product_list.html

class ProductDetailView(generic.DetailView):
   model = Product

class ProductCreate(CreateView):
   model = Product
   fields = '__all__'
   success_url = '../'
    #initial={}

class ProductUpdate(UpdateView):
   model = Product
   fields = '__all__'
   success_url = '../'

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products')
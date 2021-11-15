from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    url(r'^add/$', views.ProductCreate.as_view(), name='product_create'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product-detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ProductUpdate.as_view(), name='product_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ProductDelete.as_view(), name='product_delete'),
]
from django.conf.urls import url

from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register$', views.UserFormView.as_view(), name='register'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='product'),
    #url(r'^products/(?P<product_id>[0-9]+)/$', views.category, name='Category')
    url(r'product/add$', views.ProductCreate.as_view(), name='product-add'),
    url(r'^product/(?P<pk>[0-9]+)/update/$', views.ProductUpdate.as_view(), name='product-update'),
    url(r'^product/(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name='product-delete'),
]

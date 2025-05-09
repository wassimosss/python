from django.urls import path
from . import views
urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('products/',views.ProductList.as_view(),name='products'),
    path('products/<int:idprod>',views.ProductDetail.as_view(),name='product_detail')
]
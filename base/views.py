from django.shortcuts import render
from .products import product
from .models import Product
from django.views import View
from django.http import HttpResponse
from .forms import ProductForm
class home(View):
    def get(self,request):
        return render(request,'base/hello.html',{})
class ProductList(View):
     def get(self,request):
         products=Product.objects.all()
         return render(request,'liste.html',{'produits':products})
class ProductDetail(View):
    def get(self,request,idprod):
        product=Product.objects.get(id=idprod)
        return render(request,'detailproduct.html',{'produit':product})
class ProductCreate(View):
    def get(self,request):
        form=ProductForm()
        return render(request,'productCreate.html',{{'form':form}})
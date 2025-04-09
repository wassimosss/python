from django.shortcuts import render
from .products import product
from .models import Product
from django.views import View
from django.http import HttpResponse
class home(View):
    def get(self,request):
        return render(request,'base/hello.html',{})
class ProductList(View):
     def get(self,request):
         products=Product.objects.all()
         return render(request,'liste.html',{'produits':products})
from django.shortcuts import render # here by default
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django import forms
from django.core.exceptions import ValidationError


# Create your views here.


class HomePageView(TemplateView):
    template_name ='pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: el gran jacinto",
        
        })
        return context    

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "title": "Contact us - Online store",
        "subtitle": "Contact",
        "description": "This is an contact page ...",
        "author": "Developed by: el gran jacinto",
        "Phone":"4488123",
        "mail":"mail@mail.com"
        })
        return context 
 
class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV","pricetag":10},
        {"id":"2", "name":"iPhone", "description":"Best iPhone","pricetag":1200},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast","pricetag":1300},
        {"id":"4", "name":"Glasses", "description":"Best Glasses","pricetag":1040}
]
class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

class ProductShowView(View):

    
    template_name = 'products/show.html'
    def get(self, request, id):
        viewData = {}
        try:
            product = Product.products[int(id)-1]
        except(IndexError):
            return redirect('home')
        else:
            viewData["title"] = product["name"] + " - Online Store"
            viewData["subtitle"] = product["name"] + " - Product information"
            viewData["product"] = product
            viewData["pricetag"]=product

            return render(request, self.template_name, viewData)

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect('form')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
'''     
intento de hacer validaciones
   if form.is_valid():
            def clean(self):
                cleaned_data = super().clean()
                price=cleaned_data.get('price')
                if price>0:
                    viewData = {}
                    viewData["title"] = "Create product"
                    viewData["form"] = form
                    return render(request, self.template_name, viewData)
                else:
                    return ValidationError("el valor debe ser mayor a 1") '''
                
 
from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DeleteView

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)

def checkout(request):
    return render(request, "checkout.html")

    
class HomeView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DeleteView):
    model = Item
    template_name = "product.html"
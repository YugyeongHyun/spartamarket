from django.shortcuts import render
from django.http import HttpResponse


def products(request):
    response = HttpResponse("<h1> 나 products야 </h1>")
    return render(request, "products.html")

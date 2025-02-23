from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def eletric_product(request):
    return render(request, 'products.html')

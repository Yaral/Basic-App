from django.shortcuts import render
from django.template import loader #added as part of the project

# Create your views here.
from django.http import HttpResponse #added as part of the project
from .models import Product

#added as part of the project
def index(request):
    #return HttpResponse("Hello! You are at the products index.")
    latest_product_list = Product.objects.order_by('-product_date')[:3]
    #output = ', '.join([p.product_name for p in latest_product_list])
    template = loader.get_template('products/index.html')
    context = {
        'latest_product_list': latest_product_list,
    }
    return HttpResponse(template.render(context, request))


#added as part of the project
def detail(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)

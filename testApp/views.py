from django.shortcuts import render
from store.models import Product,ReviewRating

# Create your views here.
def dateInfo(request):
    products=Product.objects.all().filter(is_avalible=True)
    #get the Reviews
    for product in products:
        reviews=ReviewRating.objects.filter(product_id=product.id,status=True)

    context={
    'products':products,
    'reviews':reviews,
    }
    return render(request,'home.html',context)

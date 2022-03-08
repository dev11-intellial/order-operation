from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    customer = Customer.objects.values("id","first_name")
    product = Product.objects.values("id","name","unit_price")

    return render(request,'order.html',{'customer':customer,'product':product})


def order(request):
    
    if request.POST:
        cust = request.POST['cust']
        prod = request.POST['prod']

        cust_id=Customer.objects.get(id=cust)
        prod_id=Product.objects.get(id=prod)
        
        order =Order.objects.create(

            customer_id=cust_id,
            product_id =prod_id,
            price=request.POST['price'],
            qty=request.POST['quentity'],
            total_price=request.POST['totalprice']
        )
        msg = 'your order are placed'
        return redirect('orders')
    else:
        
        return render(request,'order.html')

def orders(request):

    order=Order.objects.values("id","price","qty","total_price","product_id__name","customer_id__first_name")
    customer = Customer.objects.values("id","first_name")
    product = Product.objects.values("id","name")
    return render(request,'orders.html',{'order':order,"customer":customer,"product":product})

def delete(request,id):
    order = Order.objects.get(id=id)
    order.delete()

    return redirect('orders')

def edit(request,id):
    order = Order.objects.get(id=id)
    return render(request,'edit.html',{'order':order})
    
def update(request,id):
    order = Order.objects.get(id=id)
    order.qty= request.POST['quentity']
    order.total_price = request.POST['totalprice']
    order.save()
    return redirect('orders')
    
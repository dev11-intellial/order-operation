from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    customer = Customer.objects.all()
    product = Product.objects.all()
    
    return render(request,'index.html',{'customer':customer,'product':product})


def create_order(request):
    
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
        return redirect('all_order')
    else:
        return render(request,'index.html')

def all_order(request):
    order=Order.objects.all()
    return render(request,'product.html',{'order':order})

def delete(request,id):
    order = Order.objects.get(id=id)
    order.delete()

    return redirect('all_order')

def edit(request,id):
    order = Order.objects.get(id=id)
    return render(request,'edit.html',{'order':order})
    
def update(request,id):
    order = Order.objects.get(id=id)
    order.qty= request.POST['quentity']
    order.total_price = request.POST['totalprice']
    order.save()
    return redirect('all_order')
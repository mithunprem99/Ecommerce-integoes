from django.shortcuts import render,redirect
from buyer.models import *
from seller.models import *
from siteAdmin.models import *
from django.contrib import messages
import datetime

# Create your views here.
def buyerRegistration(request):
    return render(request,'buyerRegistration.html')

def buyerhome(request):
    return render(request,'buyerhome.html')

def buyerRegistrationAction(request):
   
        name=request.POST['name']
        print(name)
        gender=request.POST['Gender']
        print(gender)
        address=request.POST['Address']
        dob=request.POST['DOB']
        country=request.POST['Country']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        buyer_db=BuyerModel(Name=name,Gender=gender,Address=address,DOB=dob,Country=country,Phone=phone,Username=username,Password=password)
        buyer_db.save()
        messages.add_message(request,messages.INFO,"Registration Sucessful")
        return render(request,'buyerhome.html')
    
def buyerEdit(request):
    buyer=request.session['id']
    buyer_db=BuyerModel.objects.filter(id=buyer)
    return render(request,'buyerEdit.html',{'editBuyer':buyer_db})

def buyerEditAction(request):
    if request.method=='POST':
        buyer=request.session['id']
        name=request.POST['Name']
        gender=request.POST.get('gender')
        address=request.POST['Address']
        dob=request.POST['DOB']
        country=request.POST['Country']
        phone=request.POST['Phone']
        username=request.POST['Username']
        password=request.POST['Password']
        buyer_db=BuyerModel.objects.filter(id=buyer).update(Name=name,Gender=gender,Address=address,DOB=dob,Country=country,Phone=phone,Username=username,Password=password)
        return redirect('buyerhome')
    else:
        return render(request,'buyerEdit.html')

def viewProductforbuyer(request):
    product_db=ProductModel.objects.all()
    # category=categoryTableModel.objects.all()
    return render(request,'viewProductforBuyer.html',{'viewproduct':product_db})

def addtoCart(request,id):
    product_db=ProductModel.objects.filter(id=id)
    messages.add_message(request,messages.INFO,"Product Added Sucessfully")
    return render(request,'addtoCart.html',{'view':product_db})


def cartView(request):
    if request.method=="POST":
        buyer=request.session['id']
        product_id=request.POST['id']
        address=request.POST['address']
        phone=request.POST['phone']
        quantity=request.POST['quantity']
        total_price=request.POST['total']
        cart_db=CartModel(Buyer_id=buyer,Product_id=product_id,Shipping=address,Phone=phone,Quantity=quantity,Total_price=total_price)
        cart_db.save()
        return redirect('viewProductforbuyer')
    else:
        return render(request,'addtoCart.html')

def viewCartProduct(request):
    buyer=request.session['id']
    cart_db=CartModel.objects.filter(Buyer_id=buyer)
    return render(request,'viewCartProduct.html',{'view':cart_db})

def cartDeleteProduct(request,id):
    cart_db=CartModel.objects.filter(id=id).delete()
    return redirect('viewCartProduct')



def placeOrder(request):
    cart_items=request.POST.getlist('checkbox')
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    for cid in cart_items:
        cart=CartModel.objects.filter(id=cid)
        buyer=request.session['id']
        stock=cart[0].Product.Stock
        product_id=cart[0].Product
        seller=cart[0].Product.Seller
        shipping=cart[0].Shipping
        quantity=cart[0].Quantity
        total_price=cart[0].Total_price
        phone=cart[0].Phone
        if quantity>int(stock):
            messages.add_message(request,messages.INFO,"Quantity is greater than stock")
            return redirect('viewCartProduct')
        else:
           
            order_db=OrderModel(Seller=seller,Product=product_id,Buyer_id=buyer,Shipping=shipping,Quantity=quantity,Total_price=total_price,Phone=phone,Date=date,Time=time)
            order_db.save()
            new_stock=int(stock)-quantity 
            product_db=ProductModel.objects.filter(id=product_id.id).update(Stock=new_stock) 
            cart.delete() 
            messages.add_message(request,messages.INFO,"order placed")
    return redirect('viewCartProduct') 

def viewCartProductforBuyer(request):
    buyer=request.session['id']
    order_db=OrderModel.objects.filter(Buyer_id=buyer)
    return render(request,'viewCartProductforBuyer.html',{'view':order_db})

def OrderCancel(request,id):
    buyer=request.session['id']
    order_db=OrderModel.objects.filter(id=id).update(Status='Cancelled')
    return redirect('viewCartProductforBuyer')

def showTrackingDetails(request,id):
    tracking_db=TrackingModel.objects.filter(Order=id)
    return render(request,'trackingDetailsforBuyer.html',{'views':tracking_db})


def searchProduct(request):
    buyer=request.session['id']
    return render(request,'searchProduct.html')

def searchProductAction(request):
    search=request.POST['search']
    product_db=ProductModel.objects.filter(Name__istartswith=search)
    return render(request,'viewProductforBuyer.html',{'viewproduct':product_db})

def searchByCategory(request):
   
    category_db=categoryTableModel.objects.all()
    return render(request,'searchByCategory.html',{'views':category_db})

def searchByCategoryAction(request):
    search=request.POST['search']
    print(search)
    price=request.POST['price']
    product_db=ProductModel.objects.filter(Price__gte=price,Category_id=search)
    return render(request,'viewProductforBuyer.html',{'viewproduct':product_db})
    


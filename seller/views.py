from django.shortcuts import render,redirect
from buyer.models import *
from seller.models import *
from siteAdmin.models import *
from django.contrib import messages
import datetime



# Create your views here.
def sellerRegistration(request):
    return render(request,'sellerRegistration.html')

def sellerhome(request):
    return render(request,'sellerhome.html')
    
def sellerRegistrationAction(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST.get('gender')
        address=request.POST['Address']
        dob=request.POST['DOB']
        country=request.POST['Country']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        

        image=request.FILES.get('file')
        seller_db=SellerModel(Name=name,Gender=gender,Address=address,DOB=dob,Country=country,Phone=phone,Username=username,Password=password,ImageFile=image)
        seller_db.save()
        messages.add_message(request,messages.INFO,"Registration Sucessful")

        return redirect('sellerhome')
    else:
        return render(request,'sellerRegistration.html')
def sellerEdit(request):
    seller=request.session['id']
    seller_db=SellerModel.objects.filter(id=seller)
    return render(request,'sellerEdit.html',{'editSeller':seller_db})

def sellerEditAction(request):
    if request.method=="POST":
        seller=request.session['id']
        sellerid=SellerModel.objects.filter(id=seller)
        name=request.POST['name']
        gender=request.POST.get('gender')
        address=request.POST['Address']
        dob=request.POST['DOB']
        country=request.POST['country']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        if len(request.FILES)>0:
            file=request.FILES['file']
        else:
            file=sellerid[0].ImageFile

        seller_db=SellerModel.objects.filter(id=seller).update(Name=name,Gender=gender,Address=address,DOB=dob,Country=country,Phone=phone,Username=username,Password=password)
        seller_object=SellerModel.objects.get(id=seller)
        seller_object.ImageFile=file
        seller_object.save()
        return redirect('sellerhome')
    else:
        return render(request,'sellerEdit.html')

def addProduct(request):
    category=categoryTableModel.objects.all()
    return render(request,'addProduct.html',{'category':category})

def addProductAction(request):
    if request.method=='POST':
        seller=request.session['id']
        name=request.POST['name']
        image=request.FILES.get('file')
        details=request.POST['details']
        stock=request.POST['stock']
        category=request.POST['category']
        price=request.POST['price']
        product_db=ProductModel(Seller_id=seller,Name=name,ImageFile=image,Details=details,Stock=stock,Category_id=category,Price=price)
        product_db.save()
        messages.add_message(request,messages.INFO,"Product Added Sucessful")

        return redirect('sellerhome')
    else:
        return render(request,'addProduct.html')

def viewAddedProduct(request):
    return render(request,'viewAddedProduct.html')

def viewAddedProductAction(request):
    seller=request.session['id']
    product=ProductModel.objects.filter(Seller_id=seller)
    return render(request,'viewAddedProduct.html',{'products':product})

def deleteProduct(request,id):
    # seller=request.session['id']
    product=ProductModel.objects.filter(id=id).delete()
    return redirect('viewAddedProductAction')

def editProduct(request,id):
    category=categoryTableModel.objects.all()
    product=ProductModel.objects.filter(id=id) 
    return render(request,'editProduct.html',{'products':product,'category':category})

def editProductAction(request):
    if request.method=='POST':
        seller=request.session['id']
        productid=request.POST['id']
        print(productid)
        product=ProductModel.objects.filter(id=productid)
        name=request.POST['name']
        details=request.POST['details']
        stock=request.POST['stock']
        category=request.POST['category']
        price=request.POST['price']
        if len(request.FILES)>0:
            file=request.FILES['file']
        else:
            file=product[0].ImageFile

        product=ProductModel.objects.filter(id=productid).update(Name=name,Details=details,Stock=stock,Category_id=category,Price=price,Seller_id=seller)
        product_object=ProductModel.objects.get(id=productid)
        product_object.ImageFile=file
        product_object.save()
        return redirect('viewAddedProductAction')
    else:
        return render(request,'editProduct.html')

    
def viewOrders(request):
    seller=request.session['id']
    order_db=OrderModel.objects.filter(Seller_id=seller)
    return render(request,'viewBuyerOrder.html',{'view':order_db})

def productApprove(request,id):
    approve=OrderModel.objects.filter(id=id).update(Status="Approved")
    return redirect('viewOrders')

def productReject(request,id):
    reject=OrderModel.objects.filter(id=id).update(Status="Rejected")
    return redirect('viewOrders')

def trackingDetails(request,id):
    order_db=OrderModel.objects.filter(id=id)
    return render(request,'orderTrackingDetails.html',{'view':order_db})

def trackingDetailsAction(request):
    if request.method=="POST":
        # order_db=OrderModel.objects.filter(id=id)
        date=date=datetime.date.today()
        time=datetime.datetime.now().strftime("%H:%M")
        details=request.POST['details']
        order_id=request.POST['id']
        tracking_db=TrackingModel(Date=date,Time=time,Details=details,Order_id=order_id)
        tracking_db.save()
        return redirect('viewOrders')
    else:
        return render(request,'orderTrackingDetails.html')

def confirmCancel(request,id):
    order_db=OrderModel.objects.filter(id=id)
    order_db.update(Status='Confirm Cancel')
    quantity=order_db[0].Quantity
    stock=order_db[0].Product.Stock
    stock=int(stock)+quantity
    product_db=ProductModel.objects.filter(id=order_db[0].Product.id)
    product_db.update(Stock=stock)
    return redirect('viewOrders')

# def logout(request):
#     return render(request,'index.html')
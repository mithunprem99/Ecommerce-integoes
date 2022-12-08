from django.shortcuts import render,redirect
from buyer.models import *
from seller.models import *
from siteAdmin.models import *
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def adminhome(request):
    return render(request,'adminhome.html')

def loginAction(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        admin_db=adminModel.objects.filter(Username=username,Password=password)
        buyer_db=BuyerModel.objects.filter(Username=username,Password=password)
        seller_db=SellerModel.objects.filter(Username=username,Password=password)
        if admin_db.count()>0:
            request.session['id']=admin_db[0].id
            return redirect('adminhome')
        
        elif buyer_db.count()>0:
            request.session['id']=buyer_db[0].id
            return redirect('buyerhome')

        elif seller_db.count()>0:
            status=seller_db[0].Status
            if status=="Approved":
                request.session['id']=seller_db[0].id
                return render(request,'sellerhome.html')
            else:
                return redirect('login')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def checkUserName(request):
    name=request.GET['name']
    buyer_db=BuyerModel.objects.filter(Username=name)
    seller_db=SellerModel.objects.filter(Username=name)
    if len(buyer_db)>0:
        msg='exist'
    elif len(seller_db)>0:
        msg='exist'
    else:
        msg='not exist'
    return JsonResponse({'valid':msg})

def adminSellerView(request):
    return render(request,'adminSellerView.html')


def viewRegisterSeller(request):
    admin=request.session['id']
    seller_db=SellerModel.objects.all()
    return render(request,'adminSellerView.html',{'viewSeller':seller_db})

def sellerApprove(request,id):
    approve=SellerModel.objects.filter(id=id).update(Status="Approved")
    return redirect('viewRegisterSeller')

def sellerReject(request,id):
    reject=SellerModel.objects.filter(id=id).update(Status="Reject")
    return redirect('viewRegisterSeller')

def categoryTable(request):
    return render(request,'categoryTable.html')

def categoryTableAction(request):
    if request.method=='POST':
        name=request.POST['name']
        admin_db=categoryTableModel(Category=name)
        admin_db.save()
        messages.add_message(request,messages.INFO,"Category Added sucessfully")

        return redirect('categoryTable')
    else:
        return render(request,'categoryTable.html')

def forgotPassword(request):
    # buyer_db=BuyerModel.objects.filter()
    return render(request,'forgotPassword.html')

def forgotPasswordAction(request):
    username=request.POST['username']
    buyer_db=BuyerModel.objects.filter(Username=username)
    if buyer_db.count()>0:
        return render(request,'newpassword.html',{'data':username})
    seller_db=SellerModel.objects.filter(Username=username)
    if seller_db.count()>0:
        return render(request,'newpassword.html',{'data':username})
    return render(request,'login.html')

def newpassword(request):
    username=request.POST['username']
    print(username)
    name=request.POST['name']
    print(name)
    country=request.POST['country']
    print(country)
    dob=request.POST['dob']
    print(dob)
    seller=SellerModel.objects.filter(Username=username,Name=name,Country=country,DOB=dob)
    print(seller)
    buyer=BuyerModel.objects.filter(Username=username,Name=name,Country=country,DOB=dob)
    print(buyer)
    if seller is not None:
        print(seller)
        return render(request,'newpasswordChange.html',{'data':username})
    elif buyer is not None:
        print(buyer)
        return render(request,'newpasswordChange.html',{'data':username})
    else:
        messages.add_message(request,messages.INFO,"incorrect data")
        return redirect('index')

def newpasswordAction(request):
    username=request.POST['username']
    password=request.POST['password']
    repassword=request.POST['repass']
    if password == repassword:
        seller_db=SellerModel.objects.filter(Username=username).update(Password=password)
        # seller_db.update(Password=password)
        buyer_db=BuyerModel.objects.filter(Username=username).update(Password=password)
        messages.add_message(request,messages.INFO,'Password Updated')
        return render(request,'login.html',{'data':username})
        
    else:
        messages.add_message(request,messages.INFO,'Password doesnt match')

        return render(request,'newpasswordChange.html')

def logout(request):
    request.session.clear()
    return redirect('index')

    


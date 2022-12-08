"""online_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteAdmin  import views as adminview
from seller import views as sellerview
from buyer import views as buyerview
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name='index'),
    path('login/',adminview.login,name='login'),
    path('loginAction/',adminview.loginAction,name='loginAction'),
    path('adminhome/',adminview.adminhome,name='adminhome'),
    path('sellerRegistration/',sellerview.sellerRegistration,name='sellerRegistration'),
    path('sellerhome/',sellerview.sellerhome,name='sellerhome'),
    path('sellerRegistrationAction/',sellerview.sellerRegistrationAction,name='sellerRegistrationAction'),
    path('buyerhome/',buyerview.buyerhome,name='buyerhome'),
    path('buyerRegistration/',buyerview.buyerRegistration,name='buyerRegistration'),
    path('buyerRegistrationAction/',buyerview.buyerRegistrationAction,name='buyerRegistrationAction'),
    path('checkUserName/',adminview.checkUserName,name='checkUserName'),
    path('adminSellerView/',adminview.adminSellerView,name='adminSellerView'),
    path('viewRegisterSeller/',adminview.viewRegisterSeller,name='viewRegisterSeller'),
    path('sellerApprove/<int:id>',adminview.sellerApprove,name='sellerApprove'),
    path('sellerReject/<int:id>',adminview.sellerReject,name='sellerReject'),
    path('categoryTable/',adminview.categoryTable,name='categoryTable'),
    path('categoryTableAction/',adminview.categoryTableAction,name='categoryTableAction'),
    path('sellerEdit/',sellerview.sellerEdit,name='sellerEdit'),
    path('sellerEditAction/',sellerview.sellerEditAction,name='sellerEditAction'),
    path('buyerEdit/',buyerview.buyerEdit,name='buyerEdit'),
    path('buyerEditAction/',buyerview.buyerEditAction,name='buyerEditAction'),
    path('addProduct/',sellerview.addProduct,name='addProduct'),
    path('addProductAction/',sellerview.addProductAction,name='addProductAction'),
    path('viewAddedProduct/',sellerview.viewAddedProduct,name='viewAddedProduct'),
    path('viewAddedProductAction/',sellerview.viewAddedProductAction,name='viewAddedProductAction'),
    path('deleteProduct/<int:id>',sellerview.deleteProduct,name='deleteProduct'),
    path('editProduct/<int:id>',sellerview.editProduct,name='editProduct'),
    path('editProductAction/',sellerview.editProductAction,name='editProductAction'),
    path('viewProductforbuyer/',buyerview.viewProductforbuyer,name='viewProductforbuyer'),
    path('addtoCart/<int:id>',buyerview.addtoCart,name='addtoCart'),
    path('cartView/',buyerview.cartView,name='cartView'),
    path('viewCartProduct/',buyerview.viewCartProduct,name='viewCartProduct'),
    path('cartDeleteProduct/<int:id>',buyerview.cartDeleteProduct,name='cartDeleteProduct'),
    path('placeOrder/',buyerview.placeOrder,name='placeOrder'),
    path('viewCartProductforBuyer/',buyerview.viewCartProductforBuyer,name='viewCartProductforBuyer'),
    path('OrderCancel/<int:id>',buyerview.OrderCancel,name='OrderCancel'),
    path('viewOrders/',sellerview.viewOrders,name='viewOrders'),
    path('productApprove/<int:id>',sellerview.productApprove,name='productApprove'),
    path('productReject/<int:id>',sellerview.productReject,name="productReject"),
    path('trackingDetails/<int:id>',sellerview.trackingDetails,name='trackingDetails'),
    path('trackingDetailsAction/',sellerview.trackingDetailsAction,name='trackingDetailsAction'),
    path('showTrackingDetails/<int:id>',buyerview.showTrackingDetails,name='showTrackingDetails'),
    path('confirmCancel/<int:id>',sellerview.confirmCancel,name='confirmCancel'),
    path('searchProduct/',buyerview.searchProduct,name='searchProduct'),
    path('searchProductAction/',buyerview.searchProductAction,name='searchProductAction'),
    path('searchByCategory/',buyerview.searchByCategory,name='searchByCategory'),
    path('searchByCategoryAction/',buyerview.searchByCategoryAction,name='searchByCategoryAction'),
    path('forgotPassword/',adminview.forgotPassword,name='forgotPassword'),
    path('forgotPasswordAction/',adminview.forgotPasswordAction,name="forgotPasswordAction"),
    path('newpassword/',adminview.newpassword,name='newpassword'),
    path('newpasswordAction/',adminview.newpasswordAction,name='newpasswordAction'),
    path('logout/',adminview.logout,name='logout')

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import (BaseView,
					ProductDetailView,
					CategoryDetailView,
					CartView,
					AddToCartView,
					DeleteFromCartView,
					ChangeQTYView,
					CheckoutView,
					MakeOrderView,
					SignUpView)


urlpatterns = [
	path('', BaseView.as_view(), name='home'),
	path('product/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
	path('category_detail/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
	path('cart/', CartView.as_view(), name='cart'),
	path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add-to-cart'),
	path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete-from-cart'),
	path('change-qty-cart/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change-qty-cart'),
	path('checkout/', CheckoutView.as_view(), name='checkout'),
	path('makeorder/', MakeOrderView.as_view(), name='make_order'),
	path('signup/', SignUpView.as_view(), name='signup' )

]
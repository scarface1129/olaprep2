from django.urls import path
from .views import Cart, Checkout,delete,payment_complete,process_payment

app_name = 'cart'

urlpatterns = [
	path('cart/', Cart.as_view(), name = 'cart'),
	path('checkout/', Checkout.as_view(), name = 'checkout'),
	path('delete/<item_id>/', delete, name = 'delete'),
	path('update/<order_id>', payment_complete, name = 'update'),
	path('payment/<order_id>', process_payment, name = 'payment'),
	# path('config/', stripe_config),  # new
]
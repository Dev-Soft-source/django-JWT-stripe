from django.urls import path
from payments.views import PaymentViewSet

urlpatterns = [
    path('create-payment-intent/', PaymentViewSet.as_view({'post': 'create'}), name='create-payment-intent'),
    path('confirm-payment/', PaymentViewSet.as_view({'post': 'confirm_payment'}), name='confirm-payment'),
    path('stripe-webhook/', PaymentViewSet.as_view({'post': 'stripe_webhook'}), name='stripe-webhook'),
]
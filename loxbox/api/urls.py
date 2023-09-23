from django.urls import path
from .views import get_transaction_states,cancel_transaction

urlpatterns = [
    path('transaction/states', get_transaction_states),
    path('transaction/<str:transaction_id>/cancel', cancel_transaction)
]
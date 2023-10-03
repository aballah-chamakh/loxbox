from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Transaction
# Create your views here.




@api_view(['GET']) 
@permission_classes([IsAuthenticated])  
def get_transaction_states(request):
    # ENSURE THAT THE CONTENT TYPE IS JSON 
    if request.content_type != 'application/json':
        return Response({"error": "Content-Type must be application/json"}, status=status.HTTP_400_BAD_REQUEST)

    # VALIDATE THE FIELD 'transaction_ids'
    transaction_ids = request.data.get('transaction_ids')
    if not transaction_ids or not isinstance(transaction_ids, list) : 
        return Response({"error": "the json body must contain a 'transaction_ids' key mapping to an array"}, status=status.HTTP_400_BAD_REQUEST)

    # GET THE ONLY THE TRANSACTIONS OF THE AUTHENTICATED CUSTOMER
    customer_obj = request.user.customer 
    customer_transactions = customer_obj.transaction_set.all()

    # POPULATE 'transaction_states' WITH STATES
    transaction_states = []
    for transaction_id in transaction_ids : 
        
        transaction_state = {'transaction_id':transaction_id,'state':'not_found'}
        if customer_transactions :
            qs = customer_transactions.filter(transaction_id=transaction_id)
            
            if qs : 
                transaction_obj = qs.first()
                transaction_state['state'] = transaction_obj.state
            
        transaction_states.append(transaction_state)
        
    return Response({"transaction_states": transaction_states},status=status.HTTP_200_OK)



# views.py

import stripe
import json
from django.conf import settings
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

import logging

logger = logging.getLogger(__name__)

from .models import Payment

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class PaymentViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    @csrf_exempt
    def create(self, request):
        try:
            data = json.loads(request.body)
            
            # Validate required fields
            if 'amount' not in data:
                return JsonResponse({'error': 'Amount is required'}, status=400)
            if 'currency' not in data:
                return JsonResponse({'error': 'Currency is required'}, status=400)
            
            # Validate amount is integer
            try:
                amount = int(data['amount'])
            except (ValueError, TypeError):
                return JsonResponse({'error': 'Amount must be an integer'}, status=400)
            
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=data['currency'],
                payment_method_types=['card'],
                payment_method="pm_card_visa",
            )
            # Return the client secret and paymentIntentId for the frontend to use with Stripe.js
            return JsonResponse({
                'clientSecret': intent['client_secret'],
                'paymentIntentId': intent['id'],
                'payment_method_id': intent['payment_method'],
            })

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            logger.exception("Error in create payment intent")  # Log the stack trace for debugging
            return JsonResponse({'error': str(e)}, status=500)

    @action(detail=False, methods=['post'])
    @csrf_exempt
    def confirm_payment(self, request):
        try:
            # Accept both JSON body and form data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.data

            payment_intent_id = data.get('payment_intent_id')
            amount = data.get('amount')

            # Validate required fields      
            if not payment_intent_id:
                return Response({'error': 'payment_intent_id is required'}, status=400)
            if not amount:
                return Response({'error': 'amount is required'}, status=400)

            # Attach payment method and confirm
            try:
                # First attach the payment method
                stripe.PaymentIntent.modify(
                    data['payment_intent_id'],
                    payment_method=data['payment_method_id']
                )
                
                # Then confirm the payment
                intent = stripe.PaymentIntent.confirm(
                    data['payment_intent_id']
                )
                
                return Response({
                    'status': intent.status,
                    'client_secret': intent.client_secret,
                    'next_action': intent.next_action
                })
                
            except stripe.error.StripeError as e:
                return Response({'error': str(e)}, status=400)
                
        except Exception as e:
            return Response({'error': f'Server error: {str(e)}'}, status=500)


    @action(detail=False, methods=['post'])
    @csrf_exempt
    def stripe_webhook(self, request):
        print("Headers:", request.META)
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        endpoint_secret = settings.STRIPE_WEBHOOK_SECRET  # Store your secret in Django settings
        
        try:
            # Construct the event from the payload and the signature
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        except ValueError as e:
            # Invalid payload
            return HttpResponseBadRequest(f"Invalid payload: {str(e)}")
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponseBadRequest(f"Invalid signature: {str(e)}")
        
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
#            order_id = payment_intent['metadata']['order_id']

            # Update the order status to 'paid' in the database
#            payment = Payment.objects.get(id=order_id)
#            payment.status = 'paid'
#            payment.transaction_id = payment_intent['id']
#            payment.amount = payment_intent['amount_received'] / 100.0
#            payment.save()

        # Once verified, handle the event type
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            print(f"PaymentIntent {payment_intent['id']} succeeded.")
            # Further processing logic (e.g., update order status, send email receipt)
        
        return HttpResponse(status=200)  # Respond with HTTP 200 for success
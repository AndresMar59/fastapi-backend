import stripe
from dotenv import load_dotenv
import os

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

payment_intents = stripe.PaymentIntent.list(limit=5)
for p in payment_intents.data:
    print(p.id, p.amount, p.status)    

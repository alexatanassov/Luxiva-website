#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, jsonify, redirect, request

import stripe
# This is your test secret API key.
stripe.api_key = 'sk_test_51PTWcfLv7h3gK4Y3Vg1TkFgJIjmGIqdBno0JvNjgr7QkBec86a68R4Dv4afIsZgb2nHIpHhgnLbYu3lJWqnx42Ef00a7Fq5qfi'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:4242'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    data = request.get_json()  # Get the data from the front-end
    try:
        session = stripe.checkout.Session.create(
            ui_mode='embedded',
            line_items=[
                {
                    'price': data['priceId'],  # Use the price ID passed from the front-end
                    'quantity': 1,
                },
            ],
            mode='payment',
            return_url=YOUR_DOMAIN + '/return.html?session_id={CHECKOUT_SESSION_ID}',
        )
    except Exception as e:
        return str(e)

    return jsonify({'id': session.id})

@app.route('/session-status', methods=['GET'])
def session_status():
  session = stripe.checkout.Session.retrieve(request.args.get('session_id'))

  return jsonify(status=session.status, customer_email=session.customer_details.email)

if __name__ == '__main__':
    app.run(port=4242)
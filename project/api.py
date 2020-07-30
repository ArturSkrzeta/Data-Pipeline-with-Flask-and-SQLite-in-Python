from flask import Flask, Response, stream_with_context
import time
import uuid
import random

APP = Flask(__name__)

currency_list = ['PLN', 'CHF', 'EUR', 'USD', 'JPY', 'CAD']

def get_transaction_details():
    transaction_id = uuid.uuid4()
    user_id = uuid.uuid4()
    amount = round(random.uniform(-10000, 10000), 2)
    currency = random.choice(currency_list)
    time.sleep(0.1)
    return transaction_id, user_id, amount, currency

def print_transaction_details(*args):
    print(*args)

@APP.route("/transactions/<int:transaction_count>", methods=["GET"])
def get_large_request(transaction_count):
    def transaction():
        for _i in range(transaction_count):
            transaction_id, user_id, amount, currency = get_transaction_details()
            print_transaction_details(transaction_id, user_id, amount, currency)
            str = f"('{transaction_id}', '{user_id}', {amount}, '{currency}')\n"
            yield str
    return Response(stream_with_context(transaction()))

if __name__ == "__main__":
    APP.run(debug=True)

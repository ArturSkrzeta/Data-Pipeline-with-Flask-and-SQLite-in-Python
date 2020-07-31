from random import choice, uniform
from uuid import uuid4
from time import sleep

currency_list = ['PLN', 'CHF', 'EUR', 'USD', 'JPY', 'CAD']

def print_transaction_details(*args):
    print(*args)

def get_transaction_details():
    transaction_id = uuid4()
    user_id = uuid4()
    amount = round(uniform(-10000, 10000), 2)
    currency = choice(currency_list)
    sleep(0.1)
    print_transaction_details(transaction_id, user_id, amount, currency)
    return transaction_id, user_id, amount, currency

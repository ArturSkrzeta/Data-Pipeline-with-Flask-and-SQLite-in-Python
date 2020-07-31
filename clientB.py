import requests
import sqlite3

endpoint = "http://127.0.0.1:5000/transactions/50"
insert_qry = "INSERT INTO tblTransactions (transaction_id, user_id, amount, currency) VALUES (?, ?, ?, ?)"
proxies = {'http': '', 'https': ''}

def connect_db_and_create_table():
    global conn, c
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute("""
                CREATE TABLE tblTransactions (
                            transaction_id text,
                            user_id text,
                            amount integer,
                            currency text
                        )
                """)
    conn.commit()

def insert_data(t):
    c.execute(insert_qry, (t[0], t[1], t[2], t[3]))
    conn.commit()

def handle_reuqest():
    with requests.get(endpoint, proxies=proxies, stream=True) as r:
        buffer = ""
        for chunk in r.iter_content(chunk_size=1):
            if chunk.endswith(b'\n'):
                t = eval(buffer)
                insert_data(t)
                buffer = ""
            else:
                buffer += chunk.decode()

def select_transaction_with_currency_filter(currency):
    select_qry = "SELECT * FROM tblTransactions WHERE currency='" + currency + "'"
    c.execute(select_qry)
    data_collection = c.fetchall()
    for data in data_collection:
        print(data)

def main():
    connect_db_and_create_table()
    handle_reuqest()
    select_transaction_with_currency_filter('PLN')

if __name__ == '__main__':
    main()

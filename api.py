from flask import Flask, Response, stream_with_context
from clientA import get_transaction_details

APP = Flask(__name__)

@APP.route("/transactions/<int:transaction_count>", methods=["GET"])
def get_large_request(transaction_count):
    def transaction():
        for _i in range(transaction_count):
            data_1, data_2, data_3, data_4 = get_transaction_details()
            yield f"('{data_1}', '{data_2}', {data_3}, '{data_4}')\n"
    return Response(stream_with_context(transaction()))

if __name__ == "__main__":
    APP.run(debug=True)

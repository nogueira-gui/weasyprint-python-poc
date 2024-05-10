import json
from flask import Flask, render_template
from interfaces.controllers.receipt_controller import ReceiptController

app = Flask(__name__)
receipt_controller = ReceiptController(app)

@app.route("/")
def index():
    receipt_json = '''{
        "company": {
            "name": "Nome da empresa LTDA",
            "cnpj": "68.640.441/0001-91",
            "address": "Av. teste, 2005 - São Paulo",
            "phone": "(11) 96555-5555"
        },
        "client": {
            "name": "John Doe",
            "address": "Rua Teste, 0 - São Paulo",
            "phone": "(11) 98888-8888"
        },
        "amount": "R$ 413,00",
        "date": "2024-05-12",
        "payment_method": "pix"
    }'''
    return render_template("index.html", receipt=json.loads(receipt_json))

if __name__ == "__main__":
    print("Starting Flask server")
    app.run(debug=True)
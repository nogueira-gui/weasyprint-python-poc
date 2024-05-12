import json
from flask import Flask, logging, render_template
from interfaces.controllers.receipt_controller import ReceiptController
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
receipt_controller = ReceiptController(app)

if not app.debug:
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

@app.route("/")
def index():
    default_json= '''{
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
    return render_template("index.html", receipt=json.loads(default_json))

if __name__ == "__main__":
    print("Starting Flask server")
    app.run(debug=True)
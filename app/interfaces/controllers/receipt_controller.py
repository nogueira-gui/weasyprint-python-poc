from flask import request, send_file, abort
from domain.use_case.html_template_filler import HTMLTemplateFiller
from domain.use_case.html_to_pdf_converter import HTMLToPDFConverter

class ReceiptController:
    def __init__(self, app):
        @app.route('/receipt', methods=['POST'])
        def convert():
            receipt = request.json

            # Validate the JSON
            required_fields = ["company", "client", "amount", "date", "payment_method"]
            for field in required_fields:
                if field not in receipt:
                    abort(400, description=f"Missing required field: {field}")

            required_company_fields = ["name", "cnpj", "address", "phone"]
            for field in required_company_fields:
                if field not in receipt["company"]:
                    abort(400, description=f"Missing required company field: {field}")

            required_client_fields = ["name", "address", "phone"]
            for field in required_client_fields:
                if field not in receipt["client"]:
                    abort(400, description=f"Missing required client field: {field}")

            html_filled = HTMLTemplateFiller.execute(receipt)
            HTMLToPDFConverter.execute(html_filled)
            #send back file to user
            return send_file("/output/output.pdf", as_attachment=True)
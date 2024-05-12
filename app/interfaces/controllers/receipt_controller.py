from flask import request, send_file, abort
from domain.use_case.html_template_filler import HTMLTemplateFiller
from domain.use_case.html_to_pdf_converter import HTMLToPDFConverter

class ReceiptController:
    def __init__(self, app):
        @app.route('/receipt', methods=['POST'])
        def convert():
            app.logger.info("POST /receipt")
            request_json = request.json
            app.logger.info(f"Request JSON: {request_json}")
            template = request_json.get("html")
            receipt = request_json.get("json")
            app.logger.info(f"Template: {template}")
            # Validate the JSON
            if template is None:
                validate_default_parameters(receipt)
                
            html_filled = HTMLTemplateFiller.execute(template, receipt)
            HTMLToPDFConverter.execute(html_filled)
            #send back file to user
            return send_file("/output/output.pdf", as_attachment=True)

        def validate_default_parameters(receipt: dict): 
            if receipt.get("company") is None:
                abort(400, "Company information not found")
            if receipt.get("client") is None:
                abort(400, "Client information not found")
            if receipt.get("amount") is None:
                abort(400, "Amount not found")
            if receipt.get("date") is None:
                abort(400, "Date not found")
            if receipt.get("payment_method") is None:
                abort(400, "Payment method not found")
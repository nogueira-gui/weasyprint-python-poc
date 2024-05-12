
import os
from interfaces.adapters.template_filler_adapter import TemplateFillerAdapter
import logging
from flask import Flask

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.logger.addHandler(logging.FileHandler('HTMLTemplateFiller.log'))

class HTMLTemplateFiller:
    def execute(template: str, receipt: dict):
        app.logger.info("Filling template")
        if template is None or template == "":
            app.logger.info("Template is None")
            payment_method = receipt.get("payment_method").lower()
            payment_method = payment_method.replace(" ", "").replace("ç", "c").replace("ã", "a").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            if payment_method == "debito" or payment_method == "credito":
                payment_method = "cartao"
            receipt["payment_method_image_path"] = os.path.abspath(f"infrastructure/assets/icons/{payment_method}.png")
        
        # app.logger.info("payment method image path added")
        template_adapter = TemplateFillerAdapter()
        html_filled =template_adapter.fill_template(template, receipt)
        app.logger.info("Template filled")
        return html_filled
        



import os
from interfaces.adapters.template_filler_adapter import TemplateFillerAdapter


class HTMLTemplateFiller:
    def execute(receipt: dict):
        print("HTMLTemplateFiller use case initialized")
        payment_method = receipt.get("payment_method").lower()
        payment_method = payment_method.replace(" ", "").replace("ç", "c").replace("ã", "a").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        if payment_method == "debito" or payment_method == "credito":
            payment_method = "cartao"
        receipt["payment_method_image_path"] = os.path.abspath(f"infrastructure/assets/icons/{payment_method}.png")
        
        template_adapter = TemplateFillerAdapter()
        html_filled =template_adapter.fill_template(receipt)
        return html_filled
        


import jinja2

import logging
from flask import Flask

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.logger.addHandler(logging.FileHandler('TemplateFillerAdapter.log'))

class TemplateFillerAdapter:
    def __init__(self):
        app.logger.info("TemplateFillerAdapter initialized")
        self.template_loader = jinja2.FileSystemLoader(searchpath="./infrastructure/jinja2_templates/")
        self.template_engine = jinja2.Environment(loader=self.template_loader)
        self.template_name = "receipt_template.html"
        
        
    def fill_template(self, template_html: str, receipt: dict):
        try:
            if template_html:
                app.logger.info("Filling template from_string")
                template = self.template_engine.from_string(template_html)
            else: 
                app.logger.info("Filling template get_template")
                template = self.template_engine.get_template(self.template_name)
            template_filled = template.render(receipt)
            app.logger.info("Template loaded")
            return template_filled
        except Exception as e:
            app.logger.error(f"Error filling template: {str(e)}")
            raise e
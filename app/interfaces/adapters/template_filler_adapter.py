import jinja2

class TemplateFillerAdapter:
    def __init__(self):
        print("TemplateFillerAdapter initialized")
        self.template_loader = jinja2.FileSystemLoader(searchpath="./infrastructure/jinja2_templates/")
        self.template_engine = jinja2.Environment(loader=self.template_loader)
        self.template_name = "receipt_template.html"
        
        
    def fill_template(self, receipt: dict):
        try:
            print(f"Filling template {self.template_name}")
            template = self.template_engine.get_template(self.template_name)
            return template.render(receipt)
        except Exception as e:
            raise e

from interfaces.adapters.weasyprint_adapter import WeasyprintAdapter


class HTMLToPDFConverter:
    def execute(html_string: str):
        print("HTMLToPDFConverter use case initialized")
        converter = WeasyprintAdapter()
        converter.convert_to_pdf(html_string, "/output/output.pdf")


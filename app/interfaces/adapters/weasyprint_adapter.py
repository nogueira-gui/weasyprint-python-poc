import os
from weasyprint import HTML

class WeasyprintAdapter:
        
    def convert_to_pdf(self, html_string:str, output_path: str):
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            HTML(string=html_string).write_pdf(output_path)
            print("PDF conversion successful")
            print(f"PDF saved at: {output_path}")
            #TODO make to return the binary file from a stream
        except Exception as e:
            print(f"PDF conversion failed: {str(e)}")
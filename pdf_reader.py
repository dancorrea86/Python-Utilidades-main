import PyPDF2

class PdfReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        texto = ""
        leitor = PyPDF2.PdfReader(self.path)
        number_of_pages = len(leitor.pages)
        for number in range(number_of_pages):
            pagina = leitor.pages[number]
            texto += pagina.extract_text()
        return texto
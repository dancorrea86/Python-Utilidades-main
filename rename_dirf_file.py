from pdf_reader import PdfReader
import os

class DirfRenamer:
    def __init__(self, path):
        self.path = path
    
    def create_new_name(self, file):
        file_complete_path = os.path.join(self.path, file)
        reader = PdfReader(file_complete_path)
        content = reader.read().split('\n')
        cnpj = content[7].replace("CNPJ: ", "").replace("/", "").replace(".", "").replace("-", "")
        new_name = f"ReciboDIRF-{cnpj}-2024.pdf"
        file_complete_path = os.path.join(self.path, new_name)
        return file_complete_path
        
    
    def rename(self):
        for file in os.listdir(self.path):
            if file.endswith('.pdf'):
                

                old_name = os.path.join(self.path, file)
                new_name = self.create_new_name(file)
                os.rename(old_name, new_name)
                print(f"Renamed {old_name} to {new_name}")

if __name__ == '__main__':
    dirf_renamer = DirfRenamer("C:\\Users\\Daniel_Maciel\\Desktop\\Declaracoes Gravadas RFB")
    dirf_renamer.rename()
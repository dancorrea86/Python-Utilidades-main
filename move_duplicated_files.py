import os
import shutil
import re
from file_lister import FileLister

class DuplicatedFilesMover:
    def __init__(self, directory):
        self.directory = directory
        self.duplicates_folder = os.path.join(directory, "duplicates")
        os.makedirs(self.duplicates_folder, exist_ok=True)
        self.seen = {}

    def listar_pdfs(self, directory):
        return [f for f in os.listdir(directory) if f.endswith(".pdf")]

    def extrair_chave(self, nome_arquivo):
        """
        Extrai a chave única (CNPJ + EmpresaID) do nome do arquivo.
        """
        padrao = r"(\d{14})"
        match = re.match(padrao, nome_arquivo)
        if match:
            return match.group(1)  # Retorna CNPJ e EmpresaID
        return None

    def mover_duplicados(self):
        lister = FileLister(self.directory, ".pdf")
        files = lister.list_files()
        vistos = {}
        pasta_duplicados = os.path.join(self.directory, "duplicado")
        os.makedirs(pasta_duplicados, exist_ok=True)
        
        for file in files:
            chave = self.extrair_chave(file)
            if chave:
                if chave in vistos:
                    shutil.move(os.path.join(self.directory, file), os.path.join(pasta_duplicados, file))
                    print(f"Movendo duplicado: {file}")
                else:
                    vistos[chave] = file
    
if __name__ == "__main__":
    directory = input("Pasta onde estão os arquivos:")
    mover = DuplicatedFilesMover(directory)
    mover.mover_duplicados()
    
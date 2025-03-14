import os

class RenameFileDeclaracaoDAS:
    def __init__(self, path):
        self.path = path

    def generate_new_name(self, old_name):
        root_cnpj = old_name.split("_")[0][0:8]
        competence = old_name.split("_")[4][0:6]
        return f"PGDASD-DECLARACAO-{root_cnpj}{competence}001.pdf"
    
    def rename(self):
        for file in os.listdir(self.path):
            if file.endswith('.pdf'):
                old_file = os.path.join(self.path, file)
                new_name = self.generate_new_name(file)
                new_file = os.path.join(self.path, new_name)
                os.rename(old_file, new_file)

if __name__ == "__main__":
    path = input("Pasta onde estão os arquivos:")
    renamer = RenameFileDeclaracaoDAS(path)
    renamer.rename()
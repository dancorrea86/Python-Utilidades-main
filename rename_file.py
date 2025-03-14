import os

class RenameFile():
    def __init__(self, directory):
        self.directory = directory

    def rename(self, new_name):
        print(f"Renaming {self.file_name} to {new_name}")
        self.file_name = new_name
            # Verifica se o diretório existe

        if not os.path.exists(self.directory):
            print(f"A pasta {self.directory} não existe.")
            return

        # Lista os arquivos da pasta
        arquivos = [f for f in os.listdir(self.directory) if f.endswith('.pdf')]

        if not arquivos:
            print("Nenhum arquivo .pdf encontrado na pasta.")
            return

        for arquivo in arquivos:
            caminho_antigo = os.path.join(self.directory, arquivo)

            try:
                # Extrai os valores fixos usando substring
                cnpj = arquivo[:14]  # CNPJ (14 primeiros caracteres)
                competencia = arquivo.split('_')[5]  # Competência (6 caracteres após "_Recibo_DCTFWEB_")

                # Novo nome do arquivo
                novo_nome = f"Recibo_{cnpj}_{competencia}_40_0000000000000000000.pdf"
                caminho_novo = os.path.join(self.directory, novo_nome)

                # Renomeia o arquivo
                os.rename(caminho_antigo, caminho_novo)
                print(f"Renomeado: {arquivo} -> {novo_nome}")
            except Exception as e:
                print(f"Erro ao renomear {arquivo}: {e}")
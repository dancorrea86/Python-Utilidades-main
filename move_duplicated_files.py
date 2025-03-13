import os
import shutil
import re

def listar_pdfs(diretorio):
    return [f for f in os.listdir(diretorio) if f.endswith(".pdf")]

def extrair_chave(nome_arquivo):
    """
    Extrai a chave única (CNPJ + EmpresaID) do nome do arquivo.
    """
    padrao = r"(\d{14})"
    match = re.match(padrao, nome_arquivo)
    if match:
        return match.group(1)  # Retorna CNPJ e EmpresaID
    return None

def mover_duplicados(diretorio):
    arquivos = listar_pdfs(diretorio)
    vistos = {}
    pasta_duplicados = os.path.join(diretorio, "duplicado")
    os.makedirs(pasta_duplicados, exist_ok=True)
    
    for arquivo in arquivos:
        chave = extrair_chave(arquivo)
        if chave:
            if chave in vistos:
                shutil.move(os.path.join(diretorio, arquivo), os.path.join(pasta_duplicados, arquivo))
                print(f"Movendo duplicado: {arquivo}")
            else:
                vistos[chave] = arquivo
    
if __name__ == "__main__":
    diretorio_alvo = "C:\\Users\\Daniel_Maciel\\Desktop\\Guias separar\\Guias"
    mover_duplicados(diretorio_alvo)
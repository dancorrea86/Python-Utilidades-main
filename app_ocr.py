import cv2
import pytesseract
import fitz  # PyMuPDF
import numpy as np
import pandas as pd
import file_lister
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  # Altere conforme o sistema



class TesseractOCR():
    
    def __init__(self, source):
        self.source = source


    def get_text(self):
        doc = fitz.open(self.source)
        texto_extraido = ""

        for i, page in enumerate(doc):
            # Renderizar a página como imagem
            pix = page.get_pixmap(dpi=300)  # Aumenta o DPI para melhor qualidade
            imagem = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)

            # Converter para escala de cinza
            imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

            # Aplicar Equalização de Histograma para melhorar contraste
            imagem_cinza = cv2.equalizeHist(imagem_cinza)

            # Aplicar Binarização adaptativa (melhor para textos com variações de iluminação)
            imagem_cinza = cv2.adaptiveThreshold(imagem_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                 cv2.THRESH_BINARY, 11, 2)

            # Aplicar um leve desfoque para redução de ruídos
            imagem_cinza = cv2.GaussianBlur(imagem_cinza, (3, 3), 0)

            # Configuração do OCR para melhor acurácia
            config = "--oem 3 --psm 6"  # Modo mais preciso para blocos de texto
            texto = pytesseract.image_to_string(imagem_cinza, lang="por", config=config)

            texto_extraido += f"\n--- Página {i+1} ---\n{texto}\n"

        return texto_extraido

if __name__ == "__main__":
    arquivos = []
    lister = file_lister.FileLister("C:\\Users\\Daniel_Maciel\\Desktop\\Nova pasta", ".pdf")
    files = lister.list_files()
    print(len(files))

    for i,file in enumerate(files):

        print(i)
        img_path = os.path.join("C:\\Users\\Daniel_Maciel\\Desktop\\Nova pasta", file)
        nome_arquivo = img_path.split("\\")[-1]
        tessOCR = TesseractOCR(img_path)
        text = tessOCR.get_text()
        linhas = text.split("\n")
        

            # Criando um dicionário com os valores extraídos
        arquivo_info = {
            "Nome do Arquivo": nome_arquivo,
            "Espaco 1": " ",
            "Espaco 2": " ",
            "Espaco 3": " ",
            "Espaco 4": " ",
            "Espaco 5": " ",
            "Espaco 6": " ",
            "Espaco 7": " ",
            "Espaco 8": " ",
            "Linha 15": linhas[15].replace(" ", "").replace(".","").replace("/","").replace("-","").split(":")[-1] if len(linhas) > 1 else "",
            "Linha 14": linhas[14].replace(" ", "").replace(".","").replace("/","").replace("-","").split(":")[-1] if len(linhas) > 1 else "",
            "Linha 13": linhas[13].replace(" ", "").replace(".","").replace("/","").replace("-","").split(":")[-1] if len(linhas) > 1 else "",
            "Linha 12": linhas[12].replace(" ", "").replace(".","").replace("/","").replace("-","").split(":")[-1] if len(linhas) > 1 else "",
            "Linha 11": linhas[11].replace(" ", "").replace(".","").replace("/","").replace("-","").split(":")[-1] if len(linhas) > 1 else "",
            "Linha 10": linhas[10].replace(" ", "").replace(".","").replace("/","").replace("-","").split(":")[-1] if len(linhas) > 1 else "",
            "Linha 9": linhas[9].replace(" ", "").replace(".","").replace("/","").replace("-","").split(":")[-1] if len(linhas) > 1 else "",
            "Linha 8": linhas[8].replace(" ", "").replace(".","").replace("/","").replace("-","").split(":")[-1] if len(linhas) > 1 else "",
            "Linha 7": linhas[7].replace(" ", "").replace(".","").replace("/","").replace("-","").split(":")[-1] if len(linhas) > 1 else "",

        }

        # Adiciona ao array de arquivos
        arquivos.append(arquivo_info)




    # Converte para DataFrame
    df = pd.DataFrame(arquivos)

    # Opcional: salvar em CSV
    df.to_csv("dados_extraidos.csv", index=False,sep=";")  


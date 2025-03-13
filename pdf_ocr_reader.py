import cv2
import pytesseract
from pdf2image import convert_from_path
import os


# Configurar o caminho do Tesseract (necessário no Windows)
# Exemplo: pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  # Altere conforme o sistema


def pdf_para_texto(pdf_path, dpi=300):
    # Converter PDF em imagens
    imagens = convert_from_path(pdf_path, dpi=dpi)

    texto_extraido = ""

    for i, imagem in enumerate(imagens):
        # Converter imagem para um array numpy (necessário para OpenCV)
        imagem_cv = cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR)

        # Converter para escala de cinza para melhorar a detecção
        imagem_cinza = cv2.cvtColor(imagem_cv, cv2.COLOR_BGR2GRAY)

        # Aplicar binarização (opcional, pode ajudar na detecção)
        imagem_cinza = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Aplicar OCR
        texto = pytesseract.image_to_string(imagem_cinza, lang="por")  # Altere "por" para "eng" se o texto for em inglês

        texto_extraido += f"\n--- Página {i+1} ---\n{texto}\n"

    return texto_extraido

if __name__ == "__main__":
    arquivo_pdf = "C:\\Users\\Daniel_Maciel\\Desktop\\Nova pasta\\33765912000103-Dirf-2025-2024-ORIGI-NORMAL.REC.pdf"  # Substitua pelo caminho do seu arquivo PDF
    texto = pdf_para_texto(arquivo_pdf)
    
    with open("texto_extraido.txt", "w", encoding="utf-8") as f:
        f.write(texto)

    print("Texto extraído e salvo em 'texto_extraido.txt'.")
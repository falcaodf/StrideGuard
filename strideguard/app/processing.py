# app/processing.py
import cv2
import numpy as np
from PIL import Image
import pytesseract
import json

def preprocess_image(pil_image: Image.Image) -> np.ndarray:
    # converte PIL -> OpenCV
    img = np.array(pil_image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # melhora contraste e aplica threshold adaptativo
    gray = cv2.equalizeHist(gray)
    th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY,11,2)
    # retorna imagem binarizada para OCR / detecção
    return th

def extract_text_from_image(processed_img: np.ndarray):
    # processed_img é uma matriz OpenCV (binarizada)
    # pytesseract espera imagem RGB/PIL
    pil = Image.fromarray(processed_img)
    # extrai texto bruto
    ocr_text = pytesseract.image_to_string(pil, lang='eng+por')
    # tentativa simples de extrair labels (linhas por nova linha)
    lines = [l.strip() for l in ocr_text.splitlines() if l.strip()]
    # elementos: heurística simples (poderias adicionar detecção de retângulos)
    elements = [{"label": l, "type": "unknown"} for l in lines]
    return ocr_text, elements

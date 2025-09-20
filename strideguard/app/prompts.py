# app/prompts.py
import json

def build_stride_prompt(ocr_text: str, elements: list) -> str:
    """
    Produz prompt que pede análise STRIDE e pede resposta em JSON.
    """
    elements_summary = json.dumps(elements, ensure_ascii=False, indent=2)
    prompt = f"""
Você recebe o texto extraído do diagrama e uma lista de elementos detectados.
Forneça uma análise de ameaças baseada na metodologia STRIDE: Spoofing, Tampering, Repudiation,
Information Disclosure, Denial of Service, Elevation of Privilege.

Regras:
- Responda estritamente em JSON válido com a chave "stride" contendo um objeto com as 6 categorias.
- Para cada categoria, gere uma lista de itens. Cada item deve ter:
  - "id": string curta
  - "description": explicação da ameaça
  - "evidence": quais palavras/elementos do diagrama suportam essa hipótese
  - "likelihood": baixo/médio/alto
  - "impact": baixo/médio/alto
  - "remediation": ações práticas e priorizadas

Entrada: 
OCR_TEXT: \"\"\"{ocr_text}\"\"\"
ELEMENTS: {elements_summary}

Retorne apenas o JSON. Não escreva comentários extras.
"""
    return prompt

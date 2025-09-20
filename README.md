# StrideGuard

O **StrideGuard** é um projeto que analisa desenhos de arquitetura de sistemas e gera um relatório automático de possíveis ameaças de segurança, usando a metodologia **STRIDE**.  

O objetivo é simples:  
- Você envia a imagem de um diagrama.  
- O sistema interpreta os elementos do desenho.  
- Ele retorna uma análise de ameaças (como spoofing, tampering, etc.) e já sugere formas de corrigir.  

---

## O que você precisa saber
- Foi feito em Python usando FastAPI.  
- Usa Inteligência Artificial do Azure (OpenAI) para pensar nos riscos.  
- Faz leitura do diagrama com OCR (reconhecimento de texto da imagem).  

---

## Como rodar
1. Clone este repositório.  
2. Instale as dependências:  
   ```bash
   pip install -r requirements.txt

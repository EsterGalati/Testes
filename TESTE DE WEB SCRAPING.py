import requests
from bs4 import BeautifulSoup
import os
import zipfile
from urllib.parse import urljoin


url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

arquivos_desejados = {
    "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
}

os.makedirs("downloads", exist_ok=True)

# Fazendo a requisição HTTP 
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrando todos os .pdf
pdf_links = []
for link in soup.find_all("a", href=True):
    href = link["href"]
    arquivo_nome = os.path.basename(href)  

    if arquivo_nome in arquivos_desejados:  
        pdf_links.append(urljoin(url, href))  

# Baixar os PDFs
def download_pdf(pdf_url, folder="downloads"):
    filename = os.path.join(folder, os.path.basename(pdf_url))  
    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Baixado: {filename}")
    else:
        print(f"Erro ao baixar: {pdf_url}")

# Baixando só os PDFs desejados
for pdf in pdf_links:
    download_pdf(pdf)

# ZIP
zip_filename = "anexos.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in os.listdir("downloads"):
        zipf.write(os.path.join("downloads", file), file)

print(f"\n📂 Todos os arquivos foram baixados e compactados em {zip_filename}")

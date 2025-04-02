import os
import zipfile
import requests
from bs4 import BeautifulSoup

def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    response = requests.get(url)
    
    # Verificar se o conteúdo retornado é um arquivo ZIP ou CSV
    if 'zip' in response.headers['Content-Type']:
        filename = url.split("/")[-1]
        file_path = os.path.join(dest_folder, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Arquivo {filename} baixado com sucesso!")
        return file_path
    elif 'csv' in response.headers['Content-Type']:
        filename = url.split("/")[-1]
        file_path = os.path.join(dest_folder, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Arquivo {filename} CSV baixado com sucesso!")
        return file_path
    else:
        print(f"Erro: O arquivo baixado não é um ZIP nem CSV. URL: {url}")
        return None

# Função para extrair arquivos ZIP
def extract_zip(zip_path, dest_folder):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(dest_folder)
        print(f"Arquivos extraídos de {zip_path} para {dest_folder}")
    except zipfile.BadZipFile:
        print(f"Erro: O arquivo {zip_path} não é um arquivo ZIP válido.")

# Função para pegar todos os arquivos .zip de uma URL
def download_all_zip_files(base_url, dest_folder):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos os links que terminam com '.zip'
    links = soup.find_all('a', href=True)
    zip_links = [link['href'] for link in links if link['href'].endswith('.zip')]

    for zip_link in zip_links:
        zip_url = base_url + zip_link
        zip_path = download_file(zip_url, dest_folder)
        if zip_path:
            extract_zip(zip_path, dest_folder)

# Função para baixar o arquivo CSV de operadoras de plano de saúde
def download_operadoras_ativas_csv(dest_folder):
    url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"
    download_file(url, dest_folder)

dest_folder = "dados_download"

# URLs para as demonstrações contábeis de 2023 e 2024
url_2024 = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/"
url_2023 = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/"

download_all_zip_files(url_2024, dest_folder)
download_all_zip_files(url_2023, dest_folder)

# Baixar o arquivo CSV das operadoras ativas
download_operadoras_ativas_csv(dest_folder)

print("Todos os arquivos foram baixados e extraídos com sucesso!")

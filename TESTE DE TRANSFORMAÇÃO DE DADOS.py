import pdfplumber
import pandas as pd
import os
import zipfile

# Arquivos
arquivo_pdf = "downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
arquivo_csv = "Rol_de_Procedimentos.csv"
arquivo_zip = "Teste_Ester.zip"

# Substituições 
substituir_abreviacoes = {
    "OD": "Procedimentos Odontológicos",
    "AMB": "Procedimentos Ambulatoriais"
}

# Tabelas extraídas
tabelas_extraidas = []

print("Abrindo o PDF e iniciando a extração...")

# Abrindo o PDF para extração
with pdfplumber.open(arquivo_pdf) as pdf:
    for pagina in pdf.pages:
        tabelas = pagina.extract_tables()
        for tabela in tabelas:
            for linha in tabela:
                if linha:  
                    linha_tratada = [str(celula).encode('utf-8').decode('utf-8', 'ignore') if celula else "" for celula in linha]
                    tabelas_extraidas.append(linha_tratada)

print(f"Extração concluída! {len(tabelas_extraidas)} linhas processadas.")

# Criando um DataFrame 
df = pd.DataFrame(tabelas_extraidas)

# Ajustando os cabeçalhos 
df.columns = df.iloc[0]  
df = df[1:].reset_index(drop=True)  

# Substituir as abreviações 
df.replace(substituir_abreviacoes, inplace=True)

# Salvando os dados no CSV 
df.to_csv(arquivo_csv, index=False, encoding="utf-8", sep=";")

print(f"Arquivo CSV '{arquivo_csv}' salvo com sucesso!")

# ZIP
with zipfile.ZipFile(arquivo_zip, "w") as zipf:
    zipf.write(arquivo_csv)

os.remove(arquivo_csv)

print(f"Processo finalizado! Arquivo compactado '{arquivo_zip}' criado com sucesso.")

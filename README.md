
## Descrição

Este repositório contém quatro testes:

1. **Web Scraping**: Download dos anexos I e II em formato PDF a partir de um site oficial e compactação em um arquivo ZIP.
2. **Transformação de Dados**: Extração dos dados da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF do Anexo I, estruturação em CSV e compactação do resultado.
3. **Análise de Dados da ANS**: Manipulação e análise de dados da Agência Nacional de Saúde Suplementar (ANS) para responder a perguntas analíticas específicas sobre as despesas das operadoras de planos de saúde.
4. **Teste de API com Vue.js e Flask**: Desenvolvimento de uma interface web utilizando Vue.js que se comunica com um servidor Python (Flask) para buscar dados de operadoras de planos de saúde a partir de um arquivo CSV.


## Teste 1 - Web Scraping

### Objetivo
Realizar o **download automático** dos arquivos PDF específicos do site da Agência Nacional de Saúde Suplementar (ANS) e compactá-los.

### Etapas do Código

1. **Acessar a página oficial da ANS** e analisar seu código HTML.
2. **Encontrar dinamicamente os links dos PDFs desejados**.
3. **Baixar os PDFs selecionados**.
4. **Salvar os arquivos na pasta `downloads/`**.
5. **Compactar os arquivos baixados em um ZIP**.

### Saída Esperada

- Um arquivo ZIP contendo:
    - `Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf`
    - `Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf`

### Bibliotecas Utilizadas

- `requests` → Para acessar a página e baixar os arquivos.
- `BeautifulSoup` → Para encontrar os links dos PDFs.
- `os` → Para manipular diretórios e arquivos.
- `zipfile` → Para compactar os arquivos.



## Teste 2 - Transformação de Dados

### Objetivo

Extrair os dados de uma **tabela estruturada** do Anexo I em PDF e salvá-los em **formato CSV**, realizando substituições de abreviações.

### Etapas do Código

1. **Abrir o PDF do Anexo I** utilizando `pdfplumber`.
2. **Ler todas as páginas** e extrair as tabelas.
3. **Criar um DataFrame** estruturado com `pandas`.
4. **Substituir as abreviações "OD" e "AMB"** por seus nomes completos.
5. **Salvar os dados em um arquivo CSV**.
6. **Compactar o CSV em um ZIP** chamado `Teste_{seu_nome}.zip`.

### Saída Esperada

- Um arquivo ZIP contendo:
    - `Rol_de_Procedimentos.csv`

### Bibliotecas Utilizadas

- `pdfplumber` → Para extrair tabelas do PDF.
- `pandas` → Para estruturar os dados.
- `os` → Para manipulação de arquivos.
- `zipfile` → Para compactação do CSV.



## Teste 3: Análise de Dados da ANS

### Objetivo

Manipulação e análise de dados da Agência Nacional de Saúde Suplementar (ANS) para responder a perguntas analíticas específicas sobre as despesas das operadoras de planos de saúde.

### Preparação dos Dados

- Download dos dados contábeis e cadastrais.
- Armazenamento dos dados em um banco de dados MySQL.
- Importação e análise dos dados via SQL.

### Queries Analíticas

- Identificação das 10 operadoras com maiores despesas em **"Eventos/Sinistros Conhecidos ou Avisados de Assistência a Saúde Médico Hospitalar"** no último trimestre e último ano.

### Ferramentas Utilizadas

- Python (`requests`, `BeautifulSoup`, `tqdm`)
- MySQL
- SQL para consultas analíticas



## Teste 4: API com Vue.js e Flask

### Funcionalidades

- Servidor Flask que processa requisições de busca textual em um arquivo CSV.
- Interface web em Vue.js para interação com o servidor.
- Endpoint para consulta de operadoras baseado em nome fantasia ou razão social.
- Coleção do Postman para testes da API.

### Tecnologias Utilizadas

- **Backend**: Python, Flask
- **Frontend**: Vue.js, Axios
- **Banco de Dados**: Arquivo CSV
- **Ferramentas de Teste**: Postman

### Instalação e Execução

#### 1. Configuração do Servidor Flask

**1.1 Instalar dependências**
```bash
pip install flask flask-cors pandas
```

**1.2 Rodar o servidor**
```bash
python server.py
```
O servidor rodará em http://127.0.0.1:5000/

#### 2. Configuração do Frontend Vue.js

**2.1 Instalar dependências**
```bash
npm install
```

**2.2 Rodar o Vue.js**
```bash
npm run serve
```
O frontend rodará em http://localhost:8080/


## Como Executar os Testes

### Instalação de Dependências

Instale as bibliotecas necessárias com:

```bash
pip install requests beautifulsoup4 pdfplumber pandas tqdm mysql-connector-python
```

### Execução

**1. Execute o Teste 1 (Web Scraping)**
```bash
python TESTE_DE_WEB_SCRAPING.py
```
- Os arquivos PDF serão baixados e compactados.

**2. Execute o Teste 2 (Transformação de Dados)**
```bash
python TESTE_DE_TRANSFORMACAO_DE_DADOS.py
```
- O arquivo CSV será gerado e compactado em um ZIP.

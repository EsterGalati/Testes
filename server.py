from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS  


app = Flask(__name__)
CORS(app)  

df = pd.read_csv("C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop.csv", 
                 sep=";", 
                 quotechar='"', 
                 encoding="utf-8")

df["CNPJ"] = df["CNPJ"].astype(str)
df["Registro_ANS"] = df["Registro_ANS"].astype(str)

df = df.fillna("")

@app.route("/buscar", methods=["GET"])
def buscar_operadora():
    """Busca operadoras pelo nome fantasia ou razão social."""
    termo = request.args.get("q", "").strip().lower()
    
    if not termo:
        return jsonify({"erro": "Nenhum termo de busca fornecido"}), 400

    resultados = df[
        df["Nome_Fantasia"].str.lower().str.contains(termo, na=False) | 
        df["Razao_Social"].str.lower().str.contains(termo, na=False)
    ]

    return jsonify(resultados.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)

    

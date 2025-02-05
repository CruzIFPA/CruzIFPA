
import ssl
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Caminho para o certificado e a chave SSL
CERT_FILE = "server.crt"
KEY_FILE = "server.key"

@app.route("/proxy", methods=["POST"])
def proxy_handler():
    # Recebe a requisição do CartBot
    data = request.json
    target_url = data.get("url")  # URL para onde o proxy deve encaminhar

    # Valida se a URL foi enviada
    if not target_url:
        return jsonify({"error": "URL é obrigatória"}), 400

    try:
        # Encaminha a requisição ao destino com SSL
        response = requests.post(
            target_url,
            json=data.get("payload"),
            headers=data.get("headers", {}),
            verify=True  # Confirma o SSL do destino
        )
        return jsonify({"status": response.status_code, "response": response.json()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Executa o proxy com suporte a SSL
    app.run(host="0.0.0.0", port=8080, ssl_context=(CERT_FILE, KEY_FILE))

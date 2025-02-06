from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WHATSAPP_API_URL = "https://graph.facebook.com/v16.0/<YOUR_PHONE_NUMBER_ID>/messages"
WHATSAPP_TOKEN = "SEU_TOKEN_DE_ACESSO"

@app.route('/webhook', methods=['POST'])
def webhook():
	data = request.json
	if not data:
		return jsonify({"error": "Invalid request"}), 400

	user_message = data.get("entry", [])[0].get("changes", [])[0].get("value", {}).get("messages", [])[0]

	if not user_message:
		return jsonify({"status": "No message to process"}), 200

	from_number = user_message.get("from")  # Número do usuário que enviou a mensagem
	message_body = user_message.get("text", {}).get("body", "")  # Texto da mensagem

	response_message = process_with_llm(message_body)

	send_whatsapp_message(from_number, response_message)

	return jsonify({"status": "success"}), 200


def send_whatsapp_message(recipient, message):
	headers = {
		"Authorization": f"Bearer {WHATSAPP_TOKEN}",
		"Content-Type": "application/json"
	}
	payload = {
		"messaging_product": "whatsapp",
		"to": recipient,
		"type": "text",
		"text": {
			"body": message
		}
	}

	response = requests.post(WHATSAPP_API_URL, headers=headers, json=payload)
	if response.status_code != 200:
		print(f"Erro ao enviar mensagem: {response.text}")
	else:
		print("Mensagem enviada com sucesso!")


def process_with_llm(user_message):
	return f"Você disse: {user_message}. Aqui está minha resposta!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)

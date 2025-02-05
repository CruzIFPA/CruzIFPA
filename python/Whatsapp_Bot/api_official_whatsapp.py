import requests
def main():
	# Configurações
	url = "https://graph.facebook.com/v16.0/<YOUR_PHONE_NUMBER_ID>/messages"
	token = "SEU_TOKEN_DE_ACESSO"
	headers = {
	    "Authorization": f"Bearer {token}",
	    "Content-Type": "application/json"
	}

	# Dados da mensagem
	data = {
	    "messaging_product": "whatsapp",
	    "to": "<NÚMERO_DO_DESTINATÁRIO>",
	    "type": "text",
	    "text": {
	        "body": "Olá! Esta é uma mensagem enviada pela API do WhatsApp."
	    }
	}

	# Enviando a mensagem
	response = requests.post(url, headers=headers, json=data)

	# Verificando a resposta
	if response.status_code == 200:
	    print("Mensagem enviada com sucesso!")
	else:
	    print(f"Erro: {response.status_code} - {response.text}")
	return 0
if __name__ == '__main__':main();

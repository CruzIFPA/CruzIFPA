from pywa import WhatsApp

def main():
	wa = WhatsApp(
	    phone_id="seu_phone_id",
	    token="seu_token_de_acesso"
	)

	wa.send_message(
	    to="numero_destino",
	    text="Olá, esta é uma mensagem de teste!"
	)
	return 0
if __name__ == '__main__':main();

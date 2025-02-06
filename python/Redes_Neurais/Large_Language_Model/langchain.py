import openai

def send_message(message):
	messages= [{"role": "user", "content": message}]
	response = openai.ChatCompletion.create(
	model='gpt-3.5-turbo',
	messages=messages,
	temperature=0
	)
	return response['choices'][0]['message']['content']
def main():
	openai.api_akey = ''
	send_message('Quem ganhou a copa do mundo de 2002?')
if __name__ == '__main__':main()

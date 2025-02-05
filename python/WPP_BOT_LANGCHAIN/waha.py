import requests

class Waha:

    def __init__(self) -> None:
        self.__api_url = 'http://url:port'
    
    def send__message(self,chat_id,message):
        url = f'{self.__api_url}/api/sendText'
        headers = {
            'Content-Type': 'aplication/json',
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
            'text': message,
        }
        requests.post(
            url=url,
        )

import os

from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import Chatgroq

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:
    def __init__(self):
        self.__chat = ChatGroq(model='llama-3.1-70b-versatile')
    
    def invoke(self, user_message):
    
        prompt = PromptTemplate(
            input_variables=['texto'],
            template='''
            Voce é um tradutor de textos do portugês para o inglês.
            <texto>
            {texto}
            </texto>
            '''
        )
        chain = prompt | self.__chat | StrOutputParser()
        response = chain.invoke({
        'texto': user_message,
        })
        return response



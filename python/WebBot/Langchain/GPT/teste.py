from langchain_community.llms import OpenAI
import openai
import sys
import argparse

def arguments():
	parser = argparse.ArgumentParser(description="««teste»»")
	parser.add_argument('-a','--api_key',required=True,help="api key")
	args = parser.parse_args()
	return args
# Configurar o proxy manualmente
openai.proxy = "http://127.0.0.1:8080"
args = arguments()
key = str(args.api_key)
# Inicializar o LLM
llm = OpenAI(
    openai_api_key=key,
    model_kwargs={}  # Aqui, você não precisa adicionar o parâmetro `proxies`
)

# Testar a LLM
response = llm.invoke("pode me ouvir?")
print(response)


"""
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import argparse
import subprocess
import time

def arguments():
		parser = argparse.ArgumentParser(description="««LLM WEBSCREPING»»")
		parser.add_argument('-t','--target',help="spicify the target URL")
		parser.add_argument('-f','--file',help="spcify the file with targets URLs")
		parser.add_argument('-a','--api_key',required=True,help="spcify the api_key")
		args = parser.parse_args()
		return args

def main():
	args = arguments()
	usr_input = input("> ")
	usr_input = str(usr_input)
	api_key = args.api_key
	proxy_url = "http://***.***.***.***:8080"
	prompt = PromptTemplate(
		input=["content"],
		template=usr_input
	)

	llm = OpenAI(
		temperature=0,
		openai_api_key=api_key,
		proxies={"http": proxy_url, "https": proxy_url}
	)
	chain = LLMChain(llm=llm, prompt=prompt)

	result = chain.run(contents=usr_input)
	print(result)

if __name__ == '__main__':main();
"""

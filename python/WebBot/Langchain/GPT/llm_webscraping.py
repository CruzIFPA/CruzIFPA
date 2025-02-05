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

class WebBot:
	def __init__(self,url):
		self.service = ChromeService(executable_path="/home/dragon/Downloads/chromedriver-linux64/chromedriver")
		self.url = url

	def main_wbb(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")  # Enable headless mode
		chrome_options.add_argument("--disable-gpu")  # Optional for compatibility
		chrome_options.add_argument("--no-sandbox")  # Recommended for Linux
		chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues
		chrome_options.add_argument("--proxy-server=http://***.***.***.***:8080")
		driver = webdriver.Chrome(service=self.service, options=chrome_options)
		driver.get(self.url)

		page_source = driver.page_source

		driver.quit()
		return page_source

def arguments():
		parser = argparse.ArgumentParser(description="««LLM WEBSCREPING»»")
		parser.add_argument('-t','--target',help="spicify the target URL")
		parser.add_argument('-v','--verbose',action="store_true" ,help="spcify the file with targets URLs")
		parser.add_argument('-f','--file',help="spcify the file with targets URLs")
		parser.add_argument('-a','--api_key',required=True ,help="spcify the file with targets URLs")
		args = parser.parse_args()
		return args

def main():
	args = arguments()
	webbot = WebBot(args.target)
	input_content = webbot.main_wbb()
	if args.verbose:
		print(f'dados de entrada {input_content}')
	api_key = args.api_key

	prompt = PromptTemplate(
		input_variables=["content"],
		template="Dado o conteúdo do site asseguir, verifique se tem alguma erro no código fonte{content}"
	)

	llm = OpenAI(temperature=0,
				 openai_api_key=args.api_key,
				 model_kwargs={"http": "http://169.254.1.1:8080", "https": "http://169.254.1.1:8080"})
	chain = LLMChain(llm=llm, prompt=prompt)

	result = chain.run(contents=input_content)
	print(result)

if __name__ == '__main__':main();
	

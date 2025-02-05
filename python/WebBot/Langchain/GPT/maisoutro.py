import openai
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a','--api_key')
args = parser.parse_args()

# Configuração da chave da API
openai.api_key = args.api_key
openai.pr
# Dados para gerar embeddings
vulnerabilidade = "SQL Injection detected in login page"

# Chamada para o endpoint de embeddings
resposta = openai.Embedding.create(
    model="text-embedding-ada-002",  # Modelo mais recente e recomendado
    input=vulnerabilidade
)

# Embedding resultante
embedding_vulnerabilidade = resposta['data'][0]['embedding']
print(embedding_vulnerabilidade)

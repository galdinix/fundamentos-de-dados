#Utilizando JSON com uma API, escreva um programa que faça uma requisição à API “cep.awesomeapi.com.br”
# passando o CEP de um endereço no Brasil conhecido por você e exiba na tela o nome da rua, 
#avenida ou travessa em questão, a cidade e o estado deste CEP.
import requests

def receber_endereco(cep):
    url =  f"https://cep.awesomeapi.com.br/json/{cep}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception: 
        print('Erro')
  
def imprimir_endereco(endereco):
    if endereco:
        print(f"CEP: {endereco['cep']}")
        print(f"Endereço: {endereco['address']}")
        print(f"Bairro: {endereco['district']}")
        print(f"Cidade: {endereco['city']}")
        print(f"Estado: {endereco['state']}")
        return
    print("Cep não encontrado")

cep = 23060420
endereco = receber_endereco(cep)
imprimir_endereco(endereco)

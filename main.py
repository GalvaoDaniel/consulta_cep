import requests

cep = input("Digite o numero do CEP que deseja buscar: ")

if len(cep) != 8:
    print('Número de CEP inválido!')
    exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

print(request.json())
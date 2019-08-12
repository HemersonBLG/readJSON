import json

dados = open('cardsStatusFeito.json', encoding='utf-8')
dados_teste = dados.read()
arquivo = json.loads(dados_teste)

for d in arquivo:
    print(d['Título'])
    print(d['Data Entrega'])
    print(d['Descrição'],'\n')

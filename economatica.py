import json
import random

"""
TODO: 
1. criar uma lista                          [X]
2. buscar um elemento por “id”              [ ] Retornar posição do objeto com o id escolhido
3. buscar um elemento por “nome”            [ ] Retornar posição do objeto com o nome escolhido
4. percorrer todos os elementos da lista    [X]
"""

jsonObjeto = "Objeto.json"
acionistaOuAplicacao = "AcionistaOuAplicacao.json"


def criarLista(arquivo_json: str, quer_acionista: bool, quer_aplicacao: bool) -> str:

    with open(arquivo_json) as file:  # arquivo_json
        data = json.load(file)

        if(arquivo_json == 'AcionistaOuAplicacao.json'):
            if quer_acionista:
                print([x for x in data if 'acionista' in x])
            if quer_aplicacao:
                print([x for x in data if 'aplicacao' in x])
        else:
            print(data)

        print("Lista percorrida:")
        for i in range(len(data)):
            print(data[i])

        print(f'\nTamanho json:\n{len(data)}')


def busca(lista, id_ou_nome, valor):
    for i in range(len(lista)):
        if(lista[i][id_ou_nome] == valor):
            return i


if __name__ == '__main__':
    
    lista = [{'id': 1, 'nome': 'Joao da Silva', 'acionista': True}, {'id': 341, 'nome': 'Antonio de Souza', 'acionista': True}, {
        'id': 31, 'nome': 'Manoel de Oliveira', 'acionista': True}, {'id': 345341, 'nome': 'Jose dos Santos', 'acionista': True}]
    
    busca = busca(lista, "id", 345341)
    
    print(busca)
    
    #criarLista(arquivo_json=acionistaOuAplicacao,quer_acionista=True, quer_aplicacao=False)

    #sorted(random.choices(range(1000), k=10))

    #resut = busca(lista, 602)

    # print(resut)

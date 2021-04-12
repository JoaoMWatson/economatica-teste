import json


class ListaPadrao:
    """Lista Padrao
    Classe responsável pelas operações principais do programa
    """

    def __init__(self, arquivo_json: str, quer_acionista: bool, quer_aplicacao: bool):
        """Iniciação da classe/construtor

        Args:
            arquivo_json (str): arquivo do qual deseja extrair os dados
            quer_acionista (bool): True para lista de acionista
            quer_aplicacao (bool): True para lista de aplicação
        """
        self.lista = []
        self.arquivo_json = arquivo_json
        self.quer_acionista = quer_acionista
        self.quer_aplicacao = quer_aplicacao

    def criar(self):
        """Método de criação das listas
        """
        with open(self.arquivo_json) as file:  # arquivo_json
            data = json.load(file)

            if(self.arquivo_json == 'AcionistaOuAplicacao.json'):
                if self.quer_acionista:
                    self.lista = [x for x in data if 'acionista' in x]
                if self.quer_aplicacao:
                    self.lista = [x for x in data if 'aplicacao' in x]
            else:
                print(data)

    def listar_todos(self):
        """Método responsável por listar todos os itens de uma lista
        """
        for i in range(len(self.lista)):
            print(self.lista[i])

    def busca_id_nome(self, id_ou_nome: str, valor):
        """Busca indice do valor escolhido

        Args:
            id_ou_nome (str): opções de busca
            valor (str/int): valor que deseja buscar

        Returns:
            int: indice do  valor procurado
        """
        for i in range(len(self.lista)):
            if(self.lista[i][id_ou_nome] == valor):
                return i

    def count(self):
        """Retorna quantidade de itens na lista

        Returns:
            int: quantidade de intens na lista
        """
        return int(len(self.lista))

    def get_item(self, index: int):
        """Item especifico a partir do index

        Args:
            index (int): index do objeto na lista

        Returns:
            dict: Objeto selecionado da lista
        """
        return self.lista[index]


if __name__ == '__main__':
    json_objeto = "Objeto.json"
    json_acionista_aplicacao = "AcionistaOuAplicacao.json"
    teste1 = ListaPadrao(json_acionista_aplicacao, True, False)
    print(teste1)

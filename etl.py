import csv
import os

path_arquivo = os.path.join(os.path.dirname(__file__), 'vendas.csv')
def ler_csv(nome_do_arquivo_csv: str) -> str:
    '''
    Funcao que le arquivo csv e retorna uma lista de dicionarios
    '''
    lista = []
    with open(nome_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)

    return lista


def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    '''
    Funcao que filtra produtos onde entregue = True
    '''
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
print(produtos_entregues)


def somar_valores_dos_produtos(lista_com_produtos_filtrado: list[dict]) -> int:
    '''
    Funcao que filtra produtos onde entregue = True
    '''
    valor_total = 0
    for produto in lista_com_produtos_filtrado:
        valor_total += int(produto.get("price"))
    return valor_total


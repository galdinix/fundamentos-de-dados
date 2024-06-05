# pip install mysql-connector-python
from conexao_bd import *
from crud import *
from menu import *

FIM = 0
conn = conectar_bd()
if (conn == None):
    print("Erro: Banco não conectado")
    exit()
opcao = menu()
while (opcao != FIM):
    match (opcao):
        case 1: incluir(conn)
        case 2: alterar(conn)
        case 3: excluir(conn)
        case 4: consultar_todos(conn)
        case 5: consultar(conn)
        case other:
            print("Erro: opção inválida")
    opcao = menu()
desconectar_bd(conn)
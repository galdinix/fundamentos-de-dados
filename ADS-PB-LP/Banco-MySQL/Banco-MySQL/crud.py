from crud_bd import *
from util import *

def incluir(conn):
    nome = entrar_nome()
    saldo = entrar_saldo()
    incluir_conta(conn, nome, saldo)

def alterar(conn):
    id = entrar_id()
    conta = consultar_conta(conn, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    operacao = entrar_operacao()
    valor = entrar_valor()
    conta = realizar_operacao(conta, operacao, valor)
    alterar_conta(conn, conta)

def realizar_operacao(conta, oper, valor):
    if (oper == "C"):
        conta[2] += valor
    else:
        conta[2] -= valor
    return conta

def excluir(conn):
    id = entrar_id()
    conta = consultar_conta(conn, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    excluir_conta(conn, id)

def consultar(conn):
    id = entrar_id()
    conta = consultar_conta(conn, id)
    if (not conta):
        print("Erro: consultar conta")
        return
    print(conta)

def consultar_todos(conn):
    contas  = consultar_contas(conn)
    for conta in contas:
        print(conta[0], conta[1], conta[2])
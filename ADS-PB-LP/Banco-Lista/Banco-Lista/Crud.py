from Util import *

def consultar_contas2(contas):
    for i in range(len(contas)):
        for j in range(len(contas[i])):
            print(contas[i][j], end=" ")
        print()

def consultar_contas(contas):
    if (not contas):
        print("Contas vazia")
        return
    for conta in contas:
        print(conta[0], conta[1], conta[2])

def consultar_conta(contas):
    if (not contas):
        print("Contas vazia")
        return
    num = int(input("Entre com o número da conta: "))
    conta = pesquisar_conta(contas, num)
    if (not conta):
        print("Erro: conta não existe")
        return
    print(conta[0], conta[1], conta[2])

def pesquisar_conta1(contas, num):
    achou = False
    for conta in contas:
        if (conta[0] == num):
            achou = True
            break
    return achou

def pesquisar_conta2(contas, num):
    pos = -1
    for i in range(len(contas)):
        if (contas[i][0] == num):
            pos = i
            break
    return pos

def pesquisar_conta(contas, num):
    conta_pesquisada = []
    for conta in contas:
        if (conta[0] == num):
            conta_pesquisada = conta
            break
    return conta_pesquisada

def incluir_conta(contas):
    num = entrar_numero_conta()
    conta = pesquisar_conta(contas, num)
    if (conta):
        print("Erro: conta já existe")
        return
    nome = input("Entre com o nome: ")
    saldo = float(input("Entre com o saldo: "))
    contas.append([num, nome, saldo])

def excluir_conta(contas):
    if (not contas):
        print("Contas vazia")
        return
    num = int(input("Entre com o número da conta: "))
    conta = pesquisar_conta(contas, num)
    if (not conta): # (conta == [])
        print("Erro: conta não existe")
        return
    if (conta[2] != 0):
        print("Erro: saldo tem que ser igual a zero")
        return
    contas.remove(conta)

def entrar_operacao():
    while (True):
        operacao = input("Entre com a operação [C]redito ou [D]ébito: ")
        operacao = operacao.upper()
        if (operacao in ("C", "D")):
            break
        else:
            print("Erro: operação inválida")
    return operacao

def entrar_valor():
    while(True):
        valor = float(input("Entre com o valor: "))
        if (valor > 0):
            break
        else:
            print("Erro: valor inválido")
    return valor

def alterar_saldo(conta, oper, valor):
    if (oper == "C"):
        conta[2] += valor
    else:
        conta[2] -= valor

def alterar_conta(contas):
    if (not contas):
        print("Contas vazia")
        return
    num = int(input("Entre com o número da conta: "))
    conta = pesquisar_conta(contas, num)
    if (not conta):
        print("Erro: conta não existe")
        return
    operacao = entrar_operacao()
    valor = entrar_valor()
    alterar_saldo(conta, operacao, valor)

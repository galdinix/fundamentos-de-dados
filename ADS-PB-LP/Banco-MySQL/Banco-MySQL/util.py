
def entrar_id():
    while (True):
        try:
            id = int(input("Entre com o id da conta: "))
            break
        except:
            print("Erro: valor inválido")
    return id

def entrar_nome():
    nome_ok = False
    while (not nome_ok):
        nome = input("Entre com o nome: ")
        if (len(nome) >= 4):
            nome_ok = True
        else:
            print("Erro: nome deve ter no mínimo 4 caracateres")
    return nome

def entrar_real(msg):
    while (True):
        try:
            real = float(input(msg))
            break
        except:
            print("Erro: valor inválido")
    return real

def entrar_saldo():
    saldo = entrar_real("Entre com o saldo: ")
    return saldo

def entrar_operacao():
    operacao_ok = False
    while (not operacao_ok):
        operacao = input("Entre com [C]redito ou [D]ebito: ").upper()
        if (operacao in ("C", "D")):
            operacao_ok = True
        else:
            print("Erro: operação inválida")
    return operacao

def entrar_valor():
    valor = entrar_real("Entre com o valor: ")
    return valor
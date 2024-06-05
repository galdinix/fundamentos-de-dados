def entrar_numero_conta():
    while (True):
        try:
            num = int(input("Entre com o número da conta: "))
            break
        except:
            print("Erro: número de conta inválido")
    return num

ARQ = "\\users\\lpmaia\\desktop\\contas.txt"

def ler_contas(contas):
    
    contas = []
    with open(ARQ, "r") as arquivo:
        linha = arquivo.readline()
        while (linha != ""):
            linha = linha.strip("\n")
            campos = linha.split(";")
            conta = [int(campos[0]), campos[1], float(campos[2])]
            contas.append(conta)
            linha = arquivo.readline()
    return contas

def gravar_contas(contas):
    with open(ARQ, "w") as arquivo:
        for conta in contas:
            arquivo.write(str(conta[0]) + ";" + conta[1] + ";" + str(conta[2]).replace(",", ".") + "\n")
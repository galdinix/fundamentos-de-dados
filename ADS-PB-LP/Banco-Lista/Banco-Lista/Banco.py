from Crud import *
from Menu import *
from Arquivos import *
from Util import *

FIM = 0
contas = ler_contas(contas = [])
opcao = menu()
while (opcao != FIM):
    match (opcao):
        case 1: incluir_conta(contas)
        case 2: alterar_conta(contas)
        case 3: excluir_conta(contas)
        case 4: consultar_contas(contas)
        case 5: consultar_conta(contas)
        case other:
            print("Erro: opção inválida")
    opcao = menu()
gravar_contas(contas)


git config --global user.email "lsgaldino27@gmail.com"
git config --global user.name "galdinix"

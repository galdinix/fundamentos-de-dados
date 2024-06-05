from conexaoBd import*
from crudBd import*
conn = conectarBanco()
if conn == None:
    print('Banco não conectado')
    exit()

contas = consultarContas(conn)
for conta in contas:
    print(conta)
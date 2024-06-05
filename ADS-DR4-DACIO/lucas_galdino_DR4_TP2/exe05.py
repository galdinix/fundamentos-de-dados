import pandas as pd

df1 = pd.read_excel('dados_exercicio05/vendas_janeiro.xlsx')
df2 = pd.read_excel('dados_exercicio05/vendas_fevereiro.xlsx')

# Combinando os DataFrames
df_combinado = pd.concat([df1, df2], ignore_index=True)
print('xlsx combinados:\n')
print(df_combinado)

contagem_vendas = df_combinado.groupby('Produto')['Quantidade'].sum().reset_index()
print('\nContagem de cada produto:\n')
print(contagem_vendas)
with pd.ExcelWriter('dados_exercicio05/contagem_vendas.xlsx') as writer:
    contagem_vendas.to_excel(writer, sheet_name='contagem-vendas-cada-produto', index=False)





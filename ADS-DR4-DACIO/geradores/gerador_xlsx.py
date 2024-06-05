import pandas as pd

# Dados de vendas para o mês de janeiro
dados_janeiro = {
    'Data': ['2024-01-01', '2024-01-05', '2024-01-10', '2024-01-15', '2024-01-20'],
    'Produto': ['Produto A', 'Produto B', 'Produto A', 'Produto C', 'Produto B'],
    'Quantidade': [10, 5, 7, 2, 4],
    'Valor': [100.0, 50.0, 70.0, 20.0, 40.0]
}
df_janeiro = pd.DataFrame(dados_janeiro)

# Dados de vendas para o mês de fevereiro
dados_fevereiro = {
    'Data': ['2024-02-02', '2024-02-06', '2024-02-11', '2024-02-16', '2024-02-21'],
    'Produto': ['Produto B', 'Produto A', 'Produto C', 'Produto A', 'Produto B'],
    'Quantidade': [8, 12, 3, 9, 6],
    'Valor': [80.0, 120.0, 30.0, 90.0, 60.0]
}
df_fevereiro = pd.DataFrame(dados_fevereiro)

# Salve os DataFrames em arquivos Excel
df_janeiro.to_excel('vendas_janeiro.xlsx', index=False)
df_fevereiro.to_excel('vendas_fevereiro.xlsx', index=False)

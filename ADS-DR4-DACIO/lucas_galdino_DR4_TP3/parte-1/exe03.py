import pandas as pd

# Carregar o arquivo CSV para um DataFrame
file_path = 'dadoSujoTP3.csv'
df = pd.read_csv(file_path)

# Verificar dados vazios
dados_vazios = df.isnull().sum()

# Verificar tipos de dados
tipos_dados = df.dtypes

# Identificar valores não numéricos na coluna 'idade'
df['idade'] = pd.to_numeric(df['idade'], errors='coerce')

# Verificar e remover linhas onde 'idade' não pode ser convertida para numérico
df = df.dropna(subset=['idade'])

# Corrigir tipos de dados de data
df['data_venda'] = pd.to_datetime(df['data_venda'], errors='coerce')
df['data_inscricao'] = pd.to_datetime(df['data_inscricao'], errors='coerce')

# Preencher valores nulos em colunas numéricas com a mediana
df['quantidade_vendida'].fillna(df['quantidade_vendida'].median(), inplace=True)
df['preco_unitario'].fillna(df['preco_unitario'].median(), inplace=True)
df['idade'].fillna(df['idade'].median(), inplace=True)

# Preencher valores nulos em colunas de texto com uma string padrão
df['telefone'].fillna('Desconhecido', inplace=True)

# Corrigir valores inconsistentes
df['email'] = df['email'].str.replace('..', '.', regex=False)

# Adicionar colunas geradas
df['total_venda_calculado'] = df['quantidade_vendida'] * df['preco_unitario']
df['mes_venda'] = df['data_venda'].dt.month

# Exportar para um arquivo Excel
arq_saida = 'dadoSujoTP3_limpo.xlsx'
df.to_excel(arq_saida, index=False)

print(df)

import pandas as pd
import pathlib

# Carregar o arquivo CSV para um DataFrame
CUR_DIR = pathlib.Path(__file__).parent.resolve()
ARQ_ENT = str(CUR_DIR) + "\\dadoSujoTP3.csv"
df = pd.read_csv(ARQ_ENT)


#para verificar o tipo dos dados
#print(df.dtypes)

# verificando se existe dados vazios no df
#print(df.isnull().sum())

#para verificar o tipo dos dados
#print(df.dtypes)

# remover nulos
df = df.dropna()
#print(df.isnull().sum())

# modificando a formatação das datas
df['data_venda'] = pd.to_datetime(df['data_venda'], errors='coerce')
df['data_inscricao'] = pd.to_datetime(df['data_inscricao'], errors='coerce')

# adicionando colunas
df['total_venda'] = df['quantidade_vendida'] * df['preco_unitario']
df['mes_venda'] = df['data_venda'].dt.month

# indo para Excel
CUR_DIR = pathlib.Path(__file__).parent.resolve()
ARQ_OUT = str(CUR_DIR) + "\\dado-limpo-TP3.xlsx"
df.to_excel(ARQ_OUT, index=False)



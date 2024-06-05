import pandas as pd
df_csv = pd.read_csv('dados_exercicio04\dados_sujos.csv')
print(df_csv.info())
df_limpo = df_csv.dropna()
df_limpo = df_limpo.dropna(axis=1)
print('\nData Frame limpo:\n')
print(df_limpo)

print('\nData Frame com nova coluna calculada, SIM para se for mulher graduada:\n')
df_limpo['mulher_graduada'] = df_limpo.apply(lambda row: 'sim' if row['sexo'] == 'F' and row['escolaridade'] == 'Graduação' else 'não', axis=1)
print(df_limpo)

df_limpo.to_csv('dados_exercicio04\dados_atualizados_04.csv', index=False)
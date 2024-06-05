import pandas as pd
from io import StringIO


filmes = {
    'Título': ['O Poderoso Chefão', 'O Senhor dos Anéis: A Sociedade do Anel', 'Forrest Gump', 'Matrix', 'Interestelar'],
    'Gênero': ['Drama', 'Fantasia', 'Drama', 'Ficção Científica', 'Ficção Científica'],
    'Ano de Lançamento': [1972, 2001, 1994, 1999, 2014]
}

df_filmes = pd.DataFrame(filmes)
print(df_filmes)

json_filmes = df_filmes.to_json(orient='records', indent=4)
print(json_filmes)

df = pd.read_json(StringIO(json_filmes))

df['Duração (min)'] = [175, 178, 142, 136, 169]
print(df)

df.to_json('dados_exercicio06/saida06.json', orient='records', indent=4)

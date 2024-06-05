import pandas as pd
import mysql.connector
import pathlib

def ler_csv(arq_leitura):
    CUR_DIR = pathlib.Path(__file__).parent.resolve()
    ARQ_ENT = str(CUR_DIR) + "\\" + arq_leitura
    df = pd.read_csv(ARQ_ENT, sep=';', encoding='utf-8', header=None)
    df.reset_index(drop=True, inplace=True)
    return df

def formatar_df_livros(df_livros):
    df_livros.columns = ['id', 'titulo', 'data_lancamento', 'preco']
    df_livros['data_lancamento'] = pd.to_datetime(df_livros['data_lancamento'], dayfirst=True).dt.strftime('%Y-%m-%d')
    return df_livros

def formatar_df_autores(df_autores):
    df_autores.columns = ['id', 'nome', 'sobrenome']
    return df_autores

def formatar_livros_autores(df_livros_autres):
    df_livros_autres.columns = ['id_livro', 'id_autor']
    return df_livros_autres

def conectar_banco():
    conn = None
    try:
        conn = mysql.connector.connect(user='root', password='l5C1SG1LD3N4*', database='biblioteca')
    except Exception as ex:
        print(ex)
    return conn

def gravar_livros(df_livros):
    sql = 'insert into livros (id, titulo, data_lancamento, preco) values (%s,%s,%s,%s);'
    conn = conectar_banco()
    cursor = conn.cursor()
    try:
        for _, linha in df_livros.iterrows():
            cursor.execute(sql, (linha['id'], linha['titulo'], linha['data_lancamento'], linha['preco']))
            conn.commit()
        print('Livro gravado com sucesso!')
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()

def gravar_autores(df_autores):
    sql = 'insert into autores (id, nome, sobrenome) values (%s,%s,%s);'
    conn = conectar_banco()
    cursor = conn.cursor()
    try:
        for _, linha in df_autores.iterrows():
            cursor.execute(sql, (linha['id'], linha['nome'], linha['sobrenome']))
            conn.commit()
        print('Autor gravado com sucesso!')
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()

def gravrar_livros_autores(df_livro_autor):
    sql = 'insert into livro_autor (id_livro, id_autor) values (%s, %s);'
    conn = conectar_banco()
    cursor = conn.cursor()
    try:
        for _, linha in df_livro_autor.iterrows():
            cursor.execute(sql, (int(linha['id_livro']), int(linha['id_autor'])))
            conn.commit()
        print('livro-autor gravado com sucesso!')
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()

def buscar_autores_por_livro(titulo_livro):
    conn = conectar_banco()
    sql = '''
    SELECT a.id, a.nome, a.sobrenome 
    FROM autores a
    JOIN livro_autor la ON a.id = la.id_autor
    JOIN livros l ON la.id_livro = l.id
    WHERE l.titulo = %s;
    '''
    try:
        df_autores = pd.read_sql(sql, conn, params=(titulo_livro,))
        conn.close()
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
        return df_autores

def buscar_livros_por_autor(nome_autor):
    conn = conectar_banco()
    sql = '''
    SELECT l.id, l.titulo, l.data_lancamento, l.preco 
    FROM livros l
    JOIN livro_autor la ON l.id = la.id_livro
    JOIN autores a ON la.id_autor = a.id
    WHERE CONCAT(a.nome, ' ', a.sobrenome) = %s;
    '''
    try:        
        df_livros = pd.read_sql(sql, conn, params=(nome_autor,))
        conn.close()
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
        return df_livros

def gravar_json_autores_de_um_livro(df):
    CUR_DIR = pathlib.Path(__file__).parent.resolve()
    ARQ_SAI = str(CUR_DIR) + "\\autores-livro.json"
    df.to_json(ARQ_SAI, orient='records', indent = 4, force_ascii=False)

def gravar_json_livros_de_um_autor(df):
    CUR_DIR = pathlib.Path(__file__).parent.resolve()
    ARQ_SAI = str(CUR_DIR) + "\\livro-autor.json"
    df.to_json(ARQ_SAI, orient='records', indent = 4, force_ascii=False)

df_livros = ler_csv('livros.csv')
df_livros = formatar_df_livros(df_livros)
gravar_livros(df_livros)

df_autores = ler_csv('autores.csv')
df_autores = formatar_df_autores(df_autores)
gravar_autores(df_autores)

df_livro_autor = ler_csv('livros-autores.csv')
df_livro_autor = formatar_livros_autores(df_livro_autor)
gravrar_livros_autores(df_livro_autor)

titulo_livro = 'Livro L1'
df_autores_livro = buscar_autores_por_livro(titulo_livro)
print('Autores do livro L1')
print(df_autores_livro)

nome_autor = 'João Maia'
df_livros_autor = buscar_livros_por_autor(nome_autor)
print('Livros do autor João Maia')
print(df_livros_autor)

gravar_json_autores_de_um_livro(df_autores_livro)
gravar_json_livros_de_um_autor(df_livros_autor)
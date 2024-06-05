import pathlib
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

def ler_csv():
    CUR_DIR = pathlib.Path(__file__).parent.resolve()
    ARQ_ENT = str(CUR_DIR) + "\\turma.csv"
    df = pd.read_csv(ARQ_ENT, header=None, sep=';', encoding='utf-8')
    df.columns = ['Nome', 'P1', 'P2', 'P3']
    return df

def alterar_notas(df):
    #df['P1'].replace(',', '.', regex= True, inplace=True)
    #df['P1'] = df['P1'].astype(float)
    df [['P1', 'P2', 'P3']] = df[['P1', 'P2', 'P3']].replace(',', '.', regex= True).astype(float)
    return df

def conectarBanco():
    conn = None
    try:
        conn = mysql.connector.connect(user='root', password='l5C1SG1LD3N4*', database='turma')
    except Exception as ex:
        print(ex)
    return conn
    
def gravar_notas(df):
    sql = 'insert into aluno (nome, P1, P2, P3) values (%s,%s,%s,%s);'
    conn = conectarBanco()
    cursor = conn.cursor()
    try:
        for linha, coluna in df.iterrows():
            cursor.execute(sql, (linha['Nome'], linha['P1'], linha['P2'], linha['P3']))
            conn.commit()
    except Exception as ex:
        
        print(ex)
    finally:
        cursor.close()

def ler_notas_bd():
    sql = 'select * from aluno;'
    conn = conectarBanco()
    df = None
    try:
        df = pd.read_sql_query(sql, conn)
        df.columns = ['Nome', 'P1', 'P2', 'P3']
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
    return df

def calcular_media(df):
    df['Media'] =  df.loc[:, ['P1', 'P2', 'P3']].mean(exis=1).round(1)
    return df

def gravar_json(df):
    CUR_DIR = pathlib.Path(__file__).parent.resolve()
    ARQ_SAI = str(CUR_DIR) + "\\aprovacao.json"
    df[['Nome', 'Media']].to_json(ARQ_SAI, orient='records', indent = 4, force_ascii=False)



df = ler_csv()
df = alterar_notas(df)
gravar_notas(df)
#df = ler_notas_bd()
#df = calcular_media(df)
#gravar_json(df)
#df.plot(kind='bar', title='Medias', x='Nome', y='Media', legend=False)
#plt.show()
#print(df)
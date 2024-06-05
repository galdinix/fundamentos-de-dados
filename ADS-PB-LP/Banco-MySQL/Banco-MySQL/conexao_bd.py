import mysql.connector
import pathlib
import configparser
CUR_DIR = pathlib.Path(__file__).parent.resolve()
ARQ_ENV = str(CUR_DIR) + "\local.env"

def ler_db_params():
    params = configparser.ConfigParser()
    params.read(ARQ_ENV)
    return params

def conectar_bd():
    conn = None
    try:
        params = ler_db_params()
        conn = mysql.connector.connect(user = params.get("DB", "username"), 
            password=params.get("DB", "password"),
            host = params.get("DB", "host"),
            port = params.get("DB", "port"),
            database = params.get("DB", "database")
        )
    except Exception as ex:
        print(ex)
    return conn

def desconectar_bd(conn):
    if (conn is not None):
        conn.close()
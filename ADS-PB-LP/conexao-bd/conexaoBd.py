import mysql.connector

def conectarBanco():
    conn = None
    try:
        conn = mysql.connector.connect(user='root', password='l5C1SG1LD3N4*', database='banco')
    except Exception as ex:
        print(ex)
    return conn
    

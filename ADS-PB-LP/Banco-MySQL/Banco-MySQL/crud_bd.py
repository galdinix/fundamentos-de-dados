
def incluir_conta(conn, nome, saldo):
    sql = "INSERT INTO contas (nome, saldo) VALUES (%s, %s);"
    cursor = conn.cursor()
    try:
        cursor.executemany(sql, [(nome, saldo)])
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()

def alterar_conta(conn, conta):
    sql = "UPDATE contas SET saldo = %s WHERE id = %s;"
    cursor = conn.cursor()
    try:
        cursor.execute(sql, [conta[2], conta[0]])
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()

def excluir_conta(conn, id):
    sql = "DELETE FROM contas WHERE id = %s;"
    cursor = conn.cursor()
    try:
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()

def consultar_conta(conn, id):
    sql = "SELECT * FROM contas WHERE id = %s;"
    cursor = conn.cursor()
    conta = []
    try:
        cursor.execute(sql, [id])
        registro = cursor.fetchall()
        if (registro):
            conta = [registro[0][0], registro[0][1], registro[0][2]]
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
    return conta

def consultar_contas(conn):
    sql = "SELECT * FROM contas;"
    cursor = conn.cursor()
    contas = []
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            contas.append([registro[0], registro[1], registro[2]])
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
    return contas

def consultarContas(conn):
    sql = 'SELECT * FROM contas;'
    cursor = conn.cursor(conn)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        contas = []
        for registro in registros:
            contas.append([registro[0], registro[1], registro[2]])
    except Exception as ex:
        print(ex)
    return contas


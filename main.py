from db import get_connection
# GETALL
""" try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('CALL consultaAlumno()')
        resultset=curso.fetchall()
        for row in resultset:
            print(row)
    connection.close()
    
except Exception as ex:
    print('error')
 """
# GETALLBYID
""" try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('CALL consultaAlumnoByID(%s)',(1))
        # row = curso.fetchone()
        resultset=curso.fetchall()
        for row in resultset:
            print(row[1])
    connection.close()
    
except Exception as ex:
    print('error')
 """
# INSERT
try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('CALL agregarAlumno(%s, %s, %s, %s)',(4, 'JJ', 'Macías', '2023-03-09 18:32:11'))
    connection.commit()
    connection.close()
    
except Exception as ex:
    print('error')
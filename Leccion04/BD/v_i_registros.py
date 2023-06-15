import psycopg2  #Esto es para pode conectarnos a Postgre

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'clara@gmail.com'),
                ('Marcos', 'Canto', 'mcanto@mail.com'),
                ('Marcelo', 'Cuenca', 'cuencaM@mail.com')
            )# Es una tupla
            cursor.executemany(sentencia, valores)  # De esta manera ejecutamos la sentencia
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son : {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
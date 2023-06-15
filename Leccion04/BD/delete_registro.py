import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Digite el numero de registro a elminar: ')
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son : {registros_eliminados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
import psycopg2  #Esto es para pode conectarnos a Postgre



#--Consulta informacion seleccionada
#--SELECT * FROM persona WHERE id_persona in (1, 2, 3)

#--Ingresamos un nuevo elemento a la tabla
#--INSERT INTO persona(nombre, apellido, email)VALUES ('Susana', 'Lara', 'slara@gmail.com')

#--Hacemos la consulta para ver toda la informacion de la tabla
#--SELECT * FROM persona

#--Sobreescribimos un elemento en la tabla
#--UPDATE persona SET nombre = 'Ivonne', apellido = 'Esperza', email = 'iesparza@email.com' WHERE id_persona = 3
#--SELECT * FROM persona
#--DELETE FROM persona WHERE id_persona = 3



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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  # Placeholder
            id_persona = input('Digite un numero para el id_persona:')
            cursor.execute(sentencia, (id_persona,))  # De esta manera ejecutamos la sentencia
            registros = cursor.fetchone()  # Recuperamos todos los registros que seran una lista
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
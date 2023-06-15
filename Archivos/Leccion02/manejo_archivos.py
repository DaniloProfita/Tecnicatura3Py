# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')  # La w es de write, utf8 para los acentos
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt. \n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('las letras son: \nr read leer, \na append anexa, \nw write escribe, \nx crea un archivo\n')
    archivo.write('t esta es para texto o text, \nb archivos binarios, \nw+ y r+ leen y escriben \n')
    archivo.write('Saludos a todos los alumnos de la tecnicatura \n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally:  # Siempre se ejecuta
    archivo.close()  # Con esto se debe cerrar el carchivo

#archivo.write('Todo quedo perfecto'): es un error porque no abrimos el archivo
archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())
#print(archivo.read(16))
#print(archivo.read(10))  #Continuamos desde la misma linea de antes
#print(archivo.readline())
#print(archivo.readline())

# Vamos a iterar el archivo, cada una de las lineas
#for linea in archivo:
    #print(linea): iteramos todos los elementos del archivo

#print(archivo.readlines()[11])  # accedemos al archivo como si fuera una lista

#Anexamos informacion, copiamos a otro
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()

print('Se ha terminado el proceso de leer y copia archivos')
#1. 1) Crear una lista que contenga nombres de ciudades del mundo 
# que contenga más de 5 elementos e imprimir por pantalla
mi_lista=['Cali','Medellin','Caicedonia','Sevilla','Armenia']

#2) Imprimir por pantalla el segundo elemento de la lista
print(mi_lista[1])

#3) Imprimir por pantalla del segundo al cuarto elemento
print(mi_lista[1:4])

#4) Visualizar el tipo de dato de la lista
print(type(mi_lista))

#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar 
# la posición del último elemento
print(mi_lista[2:])

#6) Visualizar los primeros 4 elementos de la lista
print(mi_lista[:4])

#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
mi_lista.append('Cali')
mi_lista.append('Pereira')

#8) Agregar otra ciudad, pero en la cuarta posición
mi_lista.insert(3,'Florencia')

#9) Concatenar otra lista a la ya creada
mi_lista.extend(['Orito','Palmira'])
print(mi_lista)

#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print(mi_lista.index('Cali'))

#11) ¿Qué pasa si se busca un elemento que no existe?
#print(mi_lista.index('Barranquilla'))

#12) Eliminar un elemento de la lista
mi_lista.remove('Cali')
print(mi_lista)

#13) ¿Qué pasa si el elemento a eliminar no existe?
#mi_lista.remove('Barranquilla')

#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
ultimo = mi_lista.pop()
print(ultimo)

#15) Mostrar la lista multiplicada por 4
print(mi_lista*4)


#16) Crear una tupla que contenga los números enteros del 1 al 20
tup = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

#17) Imprimir desde el índice 10 al 15 de la tupla
print(tup[10:15])

##18) Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in tup)
print(30 in tup)

#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. 
# Utilizar una variable e informar lo sucedido.
if 'Paris' in mi_lista:
    print('Very good, ya estaba en tu lista')
mi_lista.append('Paris')
print(mi_lista)


#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(mi_lista.count('Paris'))
print(tup.count(15))

#21) Convertir la tupla en una lista
lis=list(tup)
print(type(lis))

#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
a,b,c = tup[:3]
print(a,b,c)
#23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". 
# Agregar tambien otras claves, como puede ser "Pais" y "Continente".
dicc = {'Pais':'pass','Continente':'pass','Ciudad':mi_lista}
print(dicc)

#24) Imprimir las claves del diccionario
print(dicc.keys())

#25) Imprimir las ciudades a través de su clave
print(dicc.get('Ciudad'))

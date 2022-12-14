
#1) Crear una función que reciba un número como parámetro y devuelva si 
# True si es primo y False si no lo es
def isprimo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for divisores in range(2,numero//2):
        if numero % divisores == 0:
            return False
    return True


#2) Utilizando la función del punto 1, realizar otra función que reciba de 
# parámetro una lista de números y devuelva sólo aquellos que son 
# primos en otra lista
lis =[1,2,3,4,5,6,7,8,9]
def primoslista(list):
    lis1=[]
    for numero in lis:
        if isprimo(numero):
            lis1.append(numero)
    return lis1
print(primoslista(lis))

#3) Crear una función que al recibir una lista de números, 
# devuelva el que más se repite y cuántas veces lo hace. 
# Si hay más de un "más repetido", que devuelva cualquiera
a=[1,2,2,3,4,5,6,7,7,7,7,7,1,1,2,3,4,5,6,7,8,3,3]
def numero_modal(lista):
    lista_unicos=[]
    contador=[]
    if len(lista) == 0:
        return None
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            contador[i] += 1
        else:
            lista_unicos.append(elemento)
            contador.append(1)
    numero = lista_unicos[0]
    repeticiones = contador[0]
    for indice,elemento in enumerate(contador):
        if contador[indice] > repeticiones:
            numero = lista_unicos[indice]
            repeticiones = contador[indice]
    return numero, repeticiones
print(numero_modal(a))


#4) A la función del punto 3, agregar un parámetro más, que permita elegir 
# si se requiere el menor o el mayor de los mas repetidos.
def numero_modal(lista,menor):
    lista_unicos=[]
    contador=[]
    if len(lista) == 0:
        return None
    if menor:
        lista.sort()
    else:
        lista.sort(reverse=True)
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            contador[i] += 1
        else:
            lista_unicos.append(elemento)
            contador.append(1)
    numero = lista_unicos[0]
    repeticiones = contador[0]
    for indice,elemento in enumerate(contador):
        if contador[indice] > repeticiones:
            numero = lista_unicos[indice]
            repeticiones = contador[indice]
    return numero, repeticiones

a=[1,1,1,1,2,2,3,4,5,6,7,7,7,7,7,1,1,2,3,4,5,6,7,8,3,3]
numero,repeticiones = numero_modal(a,True)
print('El numero menor que mas se repite es',numero,',',repeticiones,'veces')


#5) Crear una función que convierta entre grados Celsius, Farenheit y 
# Kelvin<br>
#Fórmula 1	: (°C × 9/5) + 32 = °F<br>
#Fórmula 2	: °C + 273.15 = °K<br>
#Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de 
# destino
def  conversiones(valor,origen,destino):
    Valor_destino = 0
    if origen == 'Celsius':
        if destino == 'Celsius':
            Valor_destino= valor
        elif destino == 'Farenheit':
            Valor_destino = valor * 9/5 + 32
        elif destino ==  'Kelvin':
            Valor_destino =  valor + 273.15
        else:
            return 'La unidad de medida de destino es incorrecto'
    if origen == 'Farenheit':
        if destino == 'Farenheit':
            Valor_destino == valor
        elif destino == 'Celsius':
            Valor_destino = (valor - 32)*5/9
        elif destino == 'Kelvin':
            Valor_destino =  ((valor - 32) * 5/9) + 273.15
        else:
            return 'La unidad de medida de destino es incorrecto'
    if origen == 'Kelvin':
        if destino == 'Kelvin':
            Valor_destino == valor
        elif destino == 'Celsius':
            Valor_destino = valor - 273.15
        elif destino ==  'Farenheit':
            Valor_destino == ((valor - 273.15) * 9/5) + 32
        else:
            return 'La unidad de medida de destino es incorrecto'
    return Valor_destino, destino 

#print('0 grado Farenheit es igual a ',conversiones(0,'Farenheit','Celsius'))


#6) Iterando una lista con los tres valores posibles de temperatura que 
# recibe la función del punto 5, hacer un print para cada combinación de 
# los mismos:
a = ['Celsius','Kelvin','Farenheit']
for i in range(0,3):
    for j in range(0,3):
        print('1 grado de', a[i],'equivale a', conversiones(1,a[i],a[j]))

#7) Armar una función que devuelva el factorial de un número. Tener en 
# cuenta que el usuario puede equivocarse y enviar de parámetro un número 
# no entero o negativo

def factorial(numero):
    if numero < 0 or type(numero) != int:
        return 'Favor ingresar un numero entero positivo'
    i = 1
    fact = numero
    while (i < numero):
        fact = fact * (numero -i)
        i+=1
    return fact

for j in range(10):
    print(factorial(j), end='-----------') 

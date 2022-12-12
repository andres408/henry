'''#1) Crear una variable que contenga un elemento del conjunto 
# de números enteros y luego imprimir por pantalla si es mayor o menor a cero
a = -1
if a > 0:
    print('El numero es mayor a 0')
elif a < 0:
    print('El numero es menor a 0')
else:
    print('El numero es igual a 0')
#2. Crear dos variables y un condicional que informe si son del mismo 
# tipo de dato
b = 3
c = '4'
if type(b) == type(c):
    print('Las variables son del mismo tipo')
else:
    print('Las variables son de diferente tipo')

#3) Para los valores enteros del 1 al 20, imprimir por pantalla 
# si es par o impar
for i in range(21):
    if i % 2 == 0:
        print('El numero' , i, 'es par')
    else:
        print('El numero', i, 'es impar')
#4) En un ciclo for mostrar para los valores entre 0 y 5 
# el resultado de elevarlo a la potencia igual a 3
for i in range(6):
    print(i**3)

#5) Crear una variable que contenga un número entero 
# y realizar un ciclo for la misma cantidad de ciclos
a = 5
for i in range(a+1):
    print(i)

#6) Utilizar un ciclo while para realizar el factorial de un número guardado 
# en una variable, sólo si la variable contiene un número entero mayor a 0
a = 5
if (type(a)==int):
    if (a>0):
        factorial=a
        while(a>2):
            a -= 1
            factorial=factorial*a
        print(factorial)
    else:
        print('No es un numero positivo')
else:
    print('No es un numero entero')

#  7) Crear un ciclo for dentro de un ciclo while    
a=True
while a:
    for i in range(20):
        print(i)
        if i == 19:
            a=False     

#8) Crear un ciclo while dentro de un ciclo for

for i in range(5):
    while (i<5):
        print('Lo estamos logrando')

#9) Imprimir los números primos existentes entre 0 y 30
def primo(n):
    if n == 0 or n==1 or n == 4:
        return False
    for x in range(2,int(n/2)):
        if n%x == 0:
            return False
    return True

n = int(input('Ingrese un numero'))
for n in range(n):
    if primo(n):
        print(n,end=',')

primo = True
tope = 1000
n=0
ciclosf=0
ciclosw=0
j=0
while(n<tope):
    for x in range(2,n//2):
        if n%x ==0:
            primo =  False
            break
        j+=1
    if primo:
        print(n)
    else:
        primo = True
    n+=1
    
print('Ciclos for realizados', j)
print('Ciclos while realizados', n)   

n=0
while n<300:
    n+=1
    if n< 100:
        continue
    elif n%12 ==0:
        print(n)
    '''
n=99
while n <=300:
    if n % 3 == 0 and n % 6 == 0:
        print(n)
        break
    n+=1




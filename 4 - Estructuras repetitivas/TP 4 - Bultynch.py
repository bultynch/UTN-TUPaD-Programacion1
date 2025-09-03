#Ejercicio 1

for i in range(0, 101):
    print(i)

#Ejercicio 2

num = int(input('Ingrese un número: '))
largo = len(str(num))
print(f'El numero tiene {largo} digitos')

#Ejercicio 3

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))
suma = 0
for i in range(num1 + 1, num2 + 1):
    suma += i
print(f'La suma entre {num1} y {num2} es: {suma}')

#Ejercicio 4

total = 0
while True:
    num = int(input('Ingrese un número (0 para salir): '))
    if num == 0:
        break
    total += num
print(f'El total es: {total}')

#Ejercicio 5

import random
intentos = 0
nrandom = random.randint(0, 9)
while True:
    num = int(input('Adivine el número entre 0 y 9: '))
    intentos += 1
    if num == nrandom:
        print('Número correcto')
        break
    else:
        print('Número incorrecto, intente de nuevo')
print(f'Número de intentos: {intentos}')

#Ejercicio 6

for i in range(0, 101):
    if i % 2 == 0:
        print(i)

#Ejercicio 7

total
num = int(input('Ingrese un número: '))
for i in range(1, num + 1):
    total += i
print(f'La suma desde 1 hasta {num} es: {total}')

#Ejercicio 8

pares = 0
impares = 0
negativos = 0
positivos = 0
cero = 0
for i in range(0, 101):
    num = int(input('Ingrese el número:'))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
    else:
        cero += 1
print(f'Números pares: {pares}, Números impares: {impares}, Números negativos: {negativos}, Números positivos: {positivos}, Ceros: {cero}')

#Ejercicio 9

contador = 0
for i in range(0, 101):
    num = int(input('Ingrese un número: '))
    contador += num
print(f'El promedio es: {contador / 100}')

#Ejercicio 10

num = str(input('Ingrese un número: '))
ninvertido =  num[::-1]
print(f'El número invertido es: {ninvertido}')

#Ejercicio 1

print ('Hola Mundo!')

#Ejercicio 2

nombre = input('Ingresa tu nombre: ')
print ('Hola ' + nombre + '!')

#Ejercicio 3

nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')
pais = input('Ingresa tu país: ')
edad = input('Ingresa tu edad: ')
print ('Soy ' + nombre + ' ' + apellido + ', tengo ' + edad + ' y vivo en ' + pais)

#Ejercicio 4

import math
radio = float(input('Ingresa el radio del círculo: '))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print ('El área del círculo es: ' + str(area))
print ('El perímetro del círculo es: ' + str(perimetro))

#Ejercicio 5

segundos = int(input('Ingresa el número de segundos: '))
horas = segundos // 3600
print(segundos, 'segundos equivalen a', horas, 'horas')

#Ejercicio 6

numero = int(input('Ingresa un número: '))
n0 = numero * 0
n1 = numero * 1
n2 = numero * 2
n3 = numero * 3
n4 = numero * 4
n5 = numero * 5
n6 = numero * 6
n7 = numero * 7
n8 = numero * 8
n9 = numero * 9
print(numero, '* 0 =', n0, '\n' + 
      numero, '* 1 =', n1, '\n' + 
      numero, '* 2 =', n2, '\n' + 
      numero, '* 3 =', n3, '\n' + 
      numero, '* 4 =', n4, '\n' + 
      numero, '* 5 =', n5, '\n' + 
      numero, '* 6 =', n6, '\n' + 
      numero, '* 7 =', n7, '\n' + 
      numero, '* 8 =', n8, '\n' + 
      numero, '* 9 =', n9)

#Ejercicio 7

n1 = int(input('Ingresa el primer número distinto de cero: '))
n2 = int(input('Ingresa el segundo número distinto de cero: '))
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2
print('La suma es:', suma, '\n'+
      'La resta es:', resta, '\n' +
      'La multiplicación es:', multiplicacion, '\n' +
      'La división es:', division)

#Ejercicio 8

altura = float(input('Ingresa la altura en metros: '))
peso = float(input('Ingresa la peso en kg: '))
imc = peso / (altura ** 2)
print('El IMC es:' + imc)

#Ejercicio 9

celsius = float(input('Ingresa la temperatura en grados celsius: '))
fahrenheit = ( 9/5 * celsius) + 32
print('La temperatura en grados fahrenheit es:', fahrenheit)

#Ejercicio 10

n1 = int(input('Ingresa el primer número: '))
n2 = int(input('Ingresa el segundo número: '))
n3 = int(input('Ingresa el tercer número: '))
promedio = (n1 + n2 + n3) / 3
print('El promedio de los números es:' + promedio)
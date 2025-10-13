#Ejercicio 1

def hola_mundo():
    print('Hola Mundo')
hola_mundo()


#Ejercicio 2

def saludar_usuario(nombre):
    print(f'Hola {nombre}!')
nombre = input('Ingrese su nombre: ')
saludar_usuario(nombre)


#Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.')
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
residencia = input('Ingrese su lugar de residencia: ')
informacion_personal(nombre, apellido, edad, residencia)


#Ejercicio 4

def calcular_area_circulo(radio):
    area = 3.1416 * radio ** 2
    return area
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.1416 * radio
    return perimetro
radio = float(input('Ingrese el radio del círculo: '))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f'El área del círculo es: {area}')
print(f'El perímetro del círculo es: {perimetro}')


#Ejercicio 5

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas
segundos = int(input('Ingrese la cantidad de segundos: '))
horas = segundos_a_horas(segundos)
print(f'La cantidad de horas es: {horas}')


#Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
numero = int(input('Ingrese un número para ver su tabla de multiplicar: '))
tabla_multiplicar(numero)


#Ejercicio 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division
a = float(input('Ingrese el primer número: '))
b = float(input('Ingrese el segundo número: '))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f'Suma: {suma}')
print(f'Resta: {resta}')
print(f'Multiplicación: {multiplicacion}')
print(f'División: {division}')


#Ejercicio 8

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en metros: '))
imc = calcular_imc(peso, altura)
print(f'Su índice de masa corporal (IMC) es: {imc}')


#Ejercicio 9

def celcius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input('Ingrese la temperatura en grados Celsius: '))
fahrenheit = celcius_a_fahrenheit(celsius)
print(f'La temperatura en grados Fahrenheit es: {fahrenheit}')


#Ejercicio 10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
a = float(input('Ingrese la primera nota: '))
b = float(input('Ingrese la segunda nota: '))
c = float(input('Ingrese la tercera nota: '))
promedio = calcular_promedio(a, b, c)
print(f'El promedio de las notas es: {promedio}')

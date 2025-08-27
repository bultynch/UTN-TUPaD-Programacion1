#Ejercicio 1

edad = int(input('Ingrese su edad: '))
if edad >= 18:
    print('Es mayor de edad.')

else:
    print('Es menor de edad.')

#Ejercicio 2

nota = int(input('Ingrese su nota: '))
if nota >= 6:
    print('Aprobado.')
else:
    print('Desaprobado.')

#Ejercicio 3

num = int(input('Ingrese un número: '))
if num % 2 == 0:
    print('Ha ingresado un número par.')
else:
    print('Por favor, ingrese un número par.')

#Ejercicio 4

edad = int(input('Ingrese su edad: '))
if edad > 0 and edad < 12:
    print('Niño/a.')
elif edad >= 12 and edad < 18:
    print('Adolescente.')
elif edad >= 18 and edad < 30:
    print('Adulto/a joven.')
else:
    print('Adulto.')

#Ejercicio 5

contraseña = input('Ingrese la contraseña: ')
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print('Ha ingresado una contraseña correcta.')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres.')

#Ejercicio 6

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
mode = mode(numeros_aleatorios)
median = median(numeros_aleatorios)
mean = mean(numeros_aleatorios)

print(f'Mode: {mode}, Median: {median}, Mean: {mean}')

if mean > median > mode:
    print('La distribución tiene sesgo positivo o a la derecha.')
elif mean < median < mode:
    print('La distribución tiene sesgo negativo o a la izquierda.')
elif mean == median == mode:
    print('La distribución no tiene sesgo.')

#Ejercicio 7

frase = str(input('Ingrese una frase o palabra: '))
if frase[-1] == 'a' or frase[-1] == 'e' or frase[-1] == 'i' or frase[-1] == 'o' or frase[-1] == 'u':
    print(f'{frase} !')
else:
    print(frase)

#Ejercicio 8

nombre = str(input('Ingrese su nombre: '))
num = int(input('Ingrese un el número 1, 2 o 3: '))

if num == 1:
    print({nombre.upper})
elif num == 2:
    print({nombre.lower})
elif num == 3:
    print({nombre.title})
else:
    print('Ingrese un número válido.')

#Ejercicio 9

magnitud = float(input('Ingrese la magnitud del sismo: '))
if magnitud < 3:
    print('Muy leve.')
elif magnitud >= 3 and magnitud < 4:
    print('Leve.')
elif magnitud >= 4 and magnitud < 5:
    print('Moderado.')
elif magnitud >= 5 and magnitud < 6:
    print('Fuerte.')
elif magnitud >= 6 and magnitud < 7:
    print('Muy fuerte.')
elif magnitud >= 7:
    print('Extremo.')
else:
    print('Ingrese una magnitud válida.')

#Ejercicio 10

emisferio = str(input('Ingrese el hemisferio en el que se encuentra (Norte/Sur): '))
mes = int(input('Ingrese el mes: '))
año = int(input('Ingrese el año: '))
dia = int(input('Ingrese el día: '))

if emisferio == 'Norte' or emisferio == 'norte':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print('Invierno.')
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print('Primavera.')
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print('Verano.')
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print('Otoño.')
    else:
        print('Ingrese una fecha válida.')

elif emisferio == 'Sur' or emisferio == 'sur':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print('Verano.')
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print('Otoño.')
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print('Invierno.')
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print('Primavera.')
    else:
        print('Ingrese una fecha válida.')
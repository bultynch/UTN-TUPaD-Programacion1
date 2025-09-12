#Ejercicio 1

notas = [10, 4, 8, 7, 2, 5, 9, 3, 6, 5]
print(notas)
promedio = sum(notas) / len(notas)
notaalta = max(notas)
notabaja = min(notas)
print(f'El promedio es: {promedio}')
print(f'La nota más alta es: {notaalta}')
print(f'La nota más baja es: {notabaja}')

#Ejercicio 2

lista = []
produtos = str(input('Ingrese los 5 productos separados por comas: '))
lista = produtos.split(',')
lista.sort()
produto_eliminado = str(input('Ingrese el producto que desea quitar: '))
if produto_eliminado in lista:
    lista.remove(produto_eliminado)
    print(f'Se quitó el producto {produto_eliminado} de la lista.')

#Ejercicio 3

import random
numeros = [random.randint(1, 100)for _ in range(15)]
npares = []
nimpares = []
for numero in numeros:
    if numero % 2 == 0:
        npares.append(numero)
    else:
        nimpares.append(numero)

print(f'Lista de números: {numeros}')
print(f'Lista de números pares: {npares}')
print(f'Lista de números impares: {nimpares}')

#Ejercicio 4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sr = list(set(datos))
print(f'Lista sin repetidos: {datos_sr}')

#Ejercicio 5

estudiantes = ['Francisco', 'Augusto', 'María', 'Javier', 'Luna', 'Gabriela', 'Franco', 'Alejo']
accion = str(input('Desea agregar o quitar un estudiante?'))
if accion == 'agregar':
    nuevo_estudiante = str(input('Ingrese el nombre del estudiante a agregar: '))
    estudiantes.append(nuevo_estudiante)
    print(f'Se agregó a {nuevo_estudiante} a la lista.')
elif accion == 'quitar':
    quitar_estudiante = str(input('Ingrese el nombre del estudiante que desea quitar: '))
    estudiantes.remove(quitar_estudiante)
    print(f'Se quitó a {quitar_estudiante} de la lista.')

print(estudiantes)

#Ejercicio 6

numeros = [9, 10, 21, 30, 11, 27, 7]
numeros = [numeros[-1]] + numeros[:-1]
print(numeros)

#Ejercicio 7

temperaturas = [
    [14,22],
    [12,23],
    [16,24],
    [14,20],
    [18,21],
    [17,22],
    [16,25]
]
promedio_min = sum([temp[0] for temp in temperaturas]) / len(temperaturas)
promedio_max = sum([temp[1] for temp in temperaturas]) / len(temperaturas)
amplitud = max([temp[1] for temp in temperaturas]) - min([temp[0] for temp in temperaturas])

print(f'El promedio de las temperaturas mínimas es: {promedio_min}')
print(f'El promedio de las temperaturas máximas es: {promedio_max}')
print(f'La amplitud térmica semanal es: {amplitud}')

#Ejercicio 8

notas = [
    [6, 5, 9],
    [7, 4, 6],
    [5, 6, 3],
    [8, 9, 9],
    [9, 8, 4]
]

estudiante1 = sum(notas[0]) / len(notas[0])
estudiante2 = sum(notas[1]) / len(notas[1])
estudiante3 = sum(notas[2]) / len(notas[2])
estudiante4 = sum(notas[3]) / len(notas[3])
estudiante5 = sum(notas[4]) / len(notas[4])

print(f'El promedio del estudiante 1 es: {estudiante1}')
print(f'El promedio del estudiante 2 es: {estudiante2}')
print(f'El promedio del estudiante 3 es: {estudiante3}')
print(f'El promedio del estudiante 4 es: {estudiante4}')
print(f'El promedio del estudiante 5 es: {estudiante5}')

materia1 = sum(notas[0][0] + notas[1][0] + notas[2][0] + notas[3][0] + notas[4][0]) / len(notas)
materia2 = sum(notas[0][1] + notas[1][1] + notas[2][1] + notas[3][1] + notas[4][1]) / len(notas)
materia3 = sum(notas[0][2] + notas[1][2] + notas[2][2] + notas[3][2] + notas[4][2]) / len(notas)

print(f'El promedio de la materia 1 es: {materia1}')
print(f'El promedio de la materia 2 es: {materia2}')
print(f'El promedio de la materia 3 es: {materia3}')

#Ejercicio 9

tablero = [['-'] * 3 for _ in range(3)]
print(tablero)

while True:
    jugardor1fila = str(input('Jugador 1 (X) ingrese la fila: '))
    jugardor1columna = str(input('Jugador 1 (X) ingrese la columna: '))
    jugardor2fila = str(input('Jugador 2 (O) ingrese la fila: '))
    jugardor2columna = str(input('Jugador 2 (O) ingrese la columna: '))

    tablero[int(jugardor1fila)][int(jugardor1columna)] = 'X'
    tablero[int(jugardor2fila)][int(jugardor2columna)] = 'O'
    for fila in tablero:
        print("|".join(fila))

    if tablero[0][0] == tablero[0][1] == tablero[0][2] != '-':
        if tablero[0][0] == 'X':
            print('Gana el jugador 1')
            break
        else:
            print('Gana el jugador 2')
            break
    elif tablero[1][0] == tablero[1][1] == tablero[1][2] != '-':
        if tablero[1][0] == 'X':
            print('Gana el jugador 1')
            break
        else:
            print('Gana el jugador 2')
            break
    elif tablero[2][0] == tablero[2][1] == tablero[2][2] != '-':
        if tablero[2][0] == 'X':
            print('Gana el jugador 1')
            break
        else:
            print('Gana el jugador 2')
            break
    elif tablero[0][0] == tablero[1][0] == tablero[2][0] != '-':
        if tablero[0][0] == 'X':
            print('Gana el jugador 1')
            break
        else:
            print('Gana el jugador 2')
            break
    elif tablero[0][1] == tablero[1][1] == tablero[2][1] != '-':
        if tablero[0][1] == 'X':
            print('Gana el jugador 1')
            break
        else:
            print('Gana el jugador 2')
            break
    elif tablero[0][2] == tablero[1][2] == tablero[2][2] != '-':
        if tablero[0][2] == 'X':
            print('Gana el jugador 1')
            break
        else:
            print('Gana el jugador 2')
            break
    elif tablero[0][0] == tablero[1][1] == tablero[2][2] != '-':
        if tablero[0][0] == 'X':
            print('Gana el jugador 1')
            break
        else:
            print('Gana el jugador 2')
            break
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] != '-':
        if tablero[0][2] == 'X':
            print('Gana el jugador 1')
            break
        else:
            print('Gana el jugador 2')
            break
    

#Ejercicio 10

productos = [
    [20, 50, 34, 14, 23, 39, 45], # Producto 1
    [25, 60, 30, 10, 20, 40, 50], # Producto 2
    [30, 55, 32, 12, 22, 38, 48], # Producto 3
    [28, 58, 36, 16, 24, 37, 46]  # Producto 4
    #lun mar mie jue vie sab dom
]

sumaproductos = []
for i, dia in enumerate(productos, start=1):
    totaldia = sum(dia)
    sumaproductos.append(totaldia)
    print(f'Las ventas totales del producto {i} son {totaldia}')

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
sumadias = []
for j in range(len(productos[0])):
    sumacolumna = sum(dia[j] for dia in productos)
    sumadias.append(sumacolumna)

mayorventas = sumadias.index(max(sumadias))
print(f'El día con mayores ventas totales es el {dias[mayorventas]} con {max(sumadias)} ventas.')

masvendido = sumaproductos.index(max(sumaproductos)) + 1
print(f'El producto con más ventas es el producto {masvendido} con {max(sumaproductos)} ventas.')


    

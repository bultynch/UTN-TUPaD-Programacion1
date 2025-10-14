# Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)


#Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)


#Ejercicio 3

lista_frutas = list(precios_frutas.keys())
print(precios_frutas)


#Ejercicio 4

agenda = {
    'Alejo': '342473456',
    'Agustin': '342117432',
    'María': '3421016428',
    'Javier': '3426013888',
    'Franco': '3426556631'
}

print(agenda)
print('Número de Alejo:', agenda.get('Alejo', 'No existe'))
print('Número de Martín:', agenda.get('Martín', 'No existe'))


#Ejercicio 5

frase  = 'Hola mundo hola mundo'
palabras = frase.lower().split()
palabras_unicas = set(palabras)

contador = {}
for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print(contador)
print('Palabras únicas: ', palabras_unicas)
print('Contador de palabras: ', contador)


#Ejercicio 6

alumnos = {
    'Javier': (8.0, 7.5, 9.0),
    'Alejo': (6.0, 7.0, 5.5),
    'María': (9.5, 10.0, 9.0)
}

print(alumnos)
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f'El promedio de {nombre} es {promedio}')


#Ejercicio 7

parcial1 = {'Javier', 'Alejo', 'María', 'Martín'}
parcial2 = {'Agustin', 'Martín', 'Augusto', 'Franco'}

ambos_parciales = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
uno_de_los_dos = parcial1 | parcial2

print('Alumnos ambos parciales:', ambos_parciales)
print('Alumnos solo uno de los parciales:', solo_uno)
print('Alumnos al menos uno de los parciales:', uno_de_los_dos)


# Ejercicio 8

stock = { 'Banana': 6, 'Manzana': 10, 'Pera': 20, 'Naranja': 15}

print('Stock manzanas:', stock.get('Manzana', 10))
stock['Pera'] += 10
stock['Uva'] = 20
print(stock)


#Ejercicio 9

agenda = {
    ('Lunes', '09:00'): 'Entrega TP1',
    ('Martes', '14:00'): 'Estudiar Arquitectura',
    ('Miércoles', '10:30'): 'Salir a correr'
}

print('Evento Lunes 09:00 ->', agenda.get(('Lunes', '09:00'), 'No hay evento'))
print('Evento Martes 14:00 ->', agenda.get(('Martes', '14:00'), 'No hay evento'))
print('Evento Miércoles 12:00 ->', agenda.get(('Miércoles', '12:00'), 'No hay evento'))


#Ejercicio 10

original = {'Argentina': 'Buenos Aires','Brasil': 'Brasilia', 'Chile': 'Santiago', 'Francia': 'Paris'
}

invertido ={}

for pais, capital in original.items():
    if capital in invertido:
        if isinstance(invertido[capital], list):
            invertido[capital].append(pais)
        else:
            invertido[capital] = [invertido[capital], pais]
    else:
        invertido[capital] = pais

print(invertido)


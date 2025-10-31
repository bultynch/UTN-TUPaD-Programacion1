#Ejercicio 3

productos =[]

with open ('productos.txt', 'r') as archivo:
    for linea in archivo:
        nombre,precio,cantidad = linea.strip().split(',')
        productos.append({
            'nombre': nombre,
            'precio': float(precio),
            'cantidad': int(cantidad)
        })

print('Productos cargados: \n')
for p in productos:
    print(f'Producto: {p['nombre']}, | Precio: ${p['precio']}, | Cantidad: {p['cantidad']}')


#Ejercicio 4

nombre = input('\nIngrese el nombre del nuevo producto: ')
precio = float(input('Ingrese el precio del nuevo producto: '))
cantidad = int(input('Ingrese la cantidad del nuevo producto: '))

with open ('productos.txt', 'a') as archivo:
    archivo.write(f'{nombre},{precio},{cantidad}\n')

print('\nProducto agregado correctamente.')


#Ejercicio 5

nombre_buscar = input('\nIngrese el nombre del producto a buscar: ').lower()

encontrado = None
for p in productos:
    if p['nombre'].lower() == nombre_buscar:
        encontrado = p
        break

if encontrado:
    print(f'\nProducto encontrado: {encontrado['nombre']}, | Precio: ${encontrado['precio']}, | Cantidad: {encontrado['cantidad']}')

else:
    print('\nProducto no encontrado.')


#Ejercicio 6

productos.append({
    'nombre': nombre,
    'precio': precio,
    'cantidad': cantidad
})

with open ('productos.txt', 'w') as archivo:
    for p in productos:
        archivo.write(f'{p['nombre']},{p['precio']},{p['cantidad']}\n')

print('\nArchivo actualizado correctamente.')
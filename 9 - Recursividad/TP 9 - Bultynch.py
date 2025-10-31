#Ejercicio 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input('Ingrese un número: '))
print(f'El factorial de 1 al {num}: ')

for i in range(1, num + 1):
    print(f'{i}! = {factorial(i)}')


#Ejercicio 2

def fibonacci(n):
    if n <= 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
num = int(input('Ingrese un número: '))
print(f'La serie de Fibonacci hasta {num} es:')
for i in range(num):
    print(fibonacci(i), end=' ')


#Ejercicio 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = float(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))

print(f'{base} elevado a la {exponente} es {potencia(base, exponente)}')


#Ejercicio 4

def decimal_a_binario(n):
    if n == 0:
        return ''
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
num = int(input('Ingrese un número decimal: '))
print(f'El número {num} en binario es: {decimal_a_binario(num)}')


#Ejercicio 5

def es_palindromo(cadena):
    if len(cadena) <= 1:
        return True
    elif cadena[0] != cadena[-1]:
        return False
    else:
        return es_palindromo(cadena[1:-1])
    
palabra = input('Ingrese una palabra: ').lower()
if es_palindromo(palabra):
    print(f'La palabra "{palabra}" es un palíndromo.')
else:
    print(f'La palabra "{palabra}" no es un palíndromo.')


#Ejercicio 6

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
    
num = int(input('Ingrese un número entero positivo: '))
print(f'La suma de los dígitos es: {suma_digitos(num)}')


#Ejercicio 7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
nivel = int(input('Ingrese el número del nivel de la pirámide: '))
print(f'El número de bloques en una pirámide de {nivel} nivel/es es: {contar_bloques(nivel)}')


#Ejercicio 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
    
num = int(input('Ingrese un número entero positivo: '))
digito = int(input('Ingrese el dígito a contar: '))
print(f'El dígito {digito} aparece {contar_digito(num, digito)} veces en el número {num}.')



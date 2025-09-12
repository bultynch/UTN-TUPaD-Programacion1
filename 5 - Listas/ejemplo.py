tablero = [['-'] * 3 for _ in range(3)]

posicionesganadoras = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
]

while True:

    #imprime tablero
    for fila in tablero:
        print("|".join(fila))

    #casilla jugador 1
    jugardor1fila = int(input('Jugador 1 ingrese la fila (0,1,2): '))
    jugardor1columna = int(input('Jugador 1 ingrese la columna (0,1,2): '))

    #casilla jugador 2
    jugardor2fila = int(input('Jugador 2 ingrese la fila (0,1,2): '))
    jugardor2columna = int(input('Jugador 2 ingrese la columna (0,1,2): '))

    tablero[int(jugardor1fila)][int(jugardor1columna)] = 'X'
    tablero[int(jugardor2fila)][int(jugardor2columna)] = 'O'

    #casilla ocupada
    if tablero[jugardor1fila][jugardor1columna] == [jugardor2fila][jugardor2columna]!= '-':
        print('Casilla ocupada, intente de nuevo. \n')
        continue
    
    




    #Empate


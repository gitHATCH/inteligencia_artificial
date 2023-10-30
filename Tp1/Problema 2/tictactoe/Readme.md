# **Tic-Tac-Toe**
Esta es una implementación del clásico juego de Tic-Tac-Toe en donde un oponente es controlado por una IA que calcula el mejor movimiento teniendo en cuenta la secuencia que le de la victoria más rápido. El algoritmo Minimax es una estrategia de toma de decisiones que ayuda a la computadora a determinar el mejor movimiento posible. El juego consta de un programa en Python llamado runner.py y un módulo llamado tictactoe.py que define la lógica del juego.

### Descripción del Juego:
Se juega en una cuadrícula de 3x3, en donde dos jugadores, "X" y "O", se turnan para marcar celdas vacías. El jugador que forme línea horizontal, vertical o diagonal con su símbolo gana el juego. Si ningún jugador logra esto, el juego termina en empate.

### Algoritmo Minimax:
El algoritmo Minimax se utiliza para que la IA juegue de manera óptima. Evalúa los posibles resultados de todos los movimientos, teniendo en cuenta la mejor respuesta del oponente. El objetivo es maximizar las posibilidades de ganar de la IA mientras se minimizan las del oponente.

### Cómo Jugar:
1.Al iniciar se puede elegir jugar como "X" o "O". <br>
2.Una vez elegido, se selecciona una celda vacía para colocar una marca. <br>
3.El oponente controlado por la IA tomará una decisión utilizando el algoritmo Minimax. <br>
4.Se repite la secuencia hasta que haya algun ganador o un empate. <br>

### Acerca del Código:
El módulo tictactoe.py contiene la lógica central del juego de Tic-Tac-Toe. Sus métodos son los siguientes:

#### initial_state(): 
Este método devuelve el estado inicial del tablero, que es una matriz 3x3 con celdas vacías.

#### player(board): 
Retorna el jugador que tiene el próximo turno en el tablero. Esto se calcula contando el número de "X" y "O" en el tablero para determinar quién debe jugar a continuación.

#### actions(board): 
Devuelve un conjunto de todas las acciones posibles (i, j) disponibles en el tablero, es decir, las celdas vacías en las que se puede colocar una marca.

#### result(board, action): 
Devuelve el tablero resultante después de realizar un movimiento (i, j) en el tablero. Verifica que la celda esté vacía antes de realizar el movimiento.

#### winner(board): 
Determina al ganador del juego, si lo hay. Comprueba si algún jugador ha formado una línea horizontal, vertical o diagonal en el tablero.

#### terminal(board): 
Devuelve True si el juego ha terminado, es decir, si hay un ganador o si no hay más celdas vacías en el tablero.

#### utility(board): 
Devuelve 1 si ganó "X", -1 si "O" y 0 en caso de empate.

#### minimax(board): 
Retorna la acción óptima para el jugador actual en el tablero utilizando el algoritmo Minimax.

#### max_value(board): 
Este método se utiliza en el algoritmo Minimax y representa la elección óptima para el jugador actual. Busca el valor máximo entre las acciones disponibles. Busca lo mejor para el jugador actual.

#### min_value(board): 
Este método se utiliza en el algoritmo Minimax y representa la elección óptima para el oponente. Busca el valor mínimo entre las acciones disponibles. Busca lo peor para el otro jugador.

# **Juego de los Montones**
El Juego de Nim es un juego matemático estratégico en el que los jugadores deben quitar elementos de montones de objetos. El objetivo del juego es evitar ser el jugador que toma el último elemento. En esta implementación, se enfrenta una persona a una (IA) entrenada. El proceso de entrenamiento de la IA implica la utilización de Q-learning, una técnica de aprendizaje por refuerzo, para mejorar su capacidad de juego.

## Nim

### Inicialización del Juego
Se crea un tablero de juego que consta de montones iniciales de objetos y se establece el turno del jugador y el ganador (inicialmente no hay ganador).

#### available_actions:
Se utiliza para determinar todas las acciones disponibles en un estado dado del juego. Cada acción está representada por un par (i, j) que indica la eliminación de j elementos del montón i.

#### other_player:
Este método estático se utiliza para cambiar entre los jugadores 0 y 1.

#### switch_player:
Cambia el turno del jugador actual al otro jugador.

#### move:
El método move se utiliza para realizar un movimiento en el juego. Toma una acción (i, j) y actualiza el tablero de juego. Además, verifica si el movimiento lleva a que haya un ganador.

## NimAI

### Inicialización de la IA
La clase NimAI representa la IA que jugará. En su inicialización, se crea un diccionario q para almacenar los valores Q que representan la calidad de un estado y una acción específica. Los valores alpha y epsilon son hiperparámetros que afectan el proceso de entrenamiento.

#### update:
Este método se utiliza para actualizar el modelo de Q-learning con información sobre un movimiento específico. Toma el estado anterior, la acción tomada, el nuevo estado y la recompensa recibida para actualizar los valores Q.

#### get_q_value:
Devuelve el valor Q para un estado y una acción específica. Si no hay un valor Q existente en el diccionario, devuelve 0.

#### update_q_value: 
Se utiliza para actualizar el valor Q para un estado y una acción específica. Utiliza la fórmula del aprendizaje por refuerzo para ajustar el valor Q.

#### best_future_reward:
Este método se encarga de calcular la máxima recompensa futura posible para un estado dado. Considera todas las acciones disponibles y devuelve el valor Q más alto entre ellas.

#### choose_action:
El método choose_action se utiliza para elegir una acción en función del estado actual. Con una probabilidad epsilon, elige una acción aleatoria; de lo contrario, selecciona la acción con el valor Q más alto.

### Entrenamiento
El entrenamiento de la IA se lleva a cabo jugando un número especificado de juegos de Nim. En cada juego, la IA aprende a través del proceso de Q-learning. Los valores Q se actualizan en función de los resultados de los juegos. La IA selecciona sus movimientos utilizando la política ε-greedy, lo que significa que, con una probabilidad epsilon, realizará un movimiento aleatorio para explorar nuevas estrategias, y con probabilidad 1 - epsilon, elegirá el movimiento con el valor Q más alto.
# **Juego de los Caballeros y los Bribones**
Este juego es conocido como "Caballeros y Bribones," es un desafío lógico en el que se debe determinar quién es un caballero (siempre dice la verdad) y quién es un bribón (siempre miente) entre un conjunto de sentencias. El juego se basa en sentencias lógicas y utiliza un conjunto de reglas para deducir quién dice la verdad y quién no.

### Sentencias Lógicas:
Son afirmaciones hechas por los sujetos involucrados en este caso. Estas sentencias pueden ser verdaderas o falsas, y se utilizan para deducir la naturaleza de cada sujeto (caballero o bribón). Cada sentencia lógica está representada en el código como una combinación de símbolos lógicos, que se evalúan para determinar su veracidad.

### Resolución de los Puzzles:
El archivo puzzle.py contiene cuatro puzzles diferentes, cada uno con sus propias sentencias lógicas:

#### Puzzle 0:
En este puzzle, A afirma: "Soy tanto un caballero como un bribón." Esto es una contradicción, ya que alguien no puede ser simultáneamente un caballero y un bribón. La sentencia lógica se resuelve identificando a A como un bribón.

#### Puzzle 1:
En este caso, A afirma: "Ambos somos bribones." B no hace ninguna afirmación. Esto se resuelve observando que si A fuera un caballero, entonces su afirmación sería falsa, lo que significaría que al menos uno de ellos sería un caballero, lo cual es una contradicción. Por lo tanto, A es un bribón y B un caballero.

#### Puzzle 2:
En este puzzle, A dice: "Somos del mismo tipo." B dice: "Somos de diferentes tipos." Esto es una contradicción, ya que no pueden ser del mismo tipo y de diferentes tipos al mismo tiempo. La sentencia lógica se resuelve identificando a A como un bribón y a B como un caballero.

### Puzzle 3
En este puzzle, las declaraciones son un poco más complejas. A afirma: "Soy un caballero o soy un bribón, pero no sabes cuál." B dice: "A dijo 'Soy un bribón'." C dice: "A es un caballero." Esto se resuelve observando que si A fuera un caballero, entonces su afirmación sería verdadera, lo que significaría que es un caballero. Si A fuera un bribón, entonces su afirmación sería falsa, lo que nuevamente significaría que es un caballero. Por lo tanto, A es un caballero, B es un bribón y C es un caballero.
# **Comprensión del Contexto**
Este proyecto, es una implementación de un modelo de lenguaje pre-entrenado utilizando BERT (Bidirectional Encoder Representations from Transformers) para completar palabras o frases enmascaradas en un texto. BERT es uno de los modelos de lenguaje más avanzados en la actualidad, desarrollado por Google, y se pre-entrena en grandes cantidades de texto antes de ser afinado para tareas específicas. El programa recibe texto con [MASK], reemplaza [MASK] con palabras o frases sugeridas por el modelo y visualiza la atención del modelo para comprender su proceso de toma de decisiones.

## Uso
El programa mask.py solicitará ingresar un texto que contenga [MASK]. A continuación, realizará las siguientes tareas:

Tokenización del texto de entrada utilizando un modelo BERT pre-entrenado.
Reemplazo de [MASK] con palabras sugeridas por el modelo.
Visualización de la atención del modelo para comprender las relaciones entre las palabras en el contexto.

## Componentes
El programa consta de varios componentes clave que desempeñan un papel fundamental en el proceso:

#### Modelo de Lenguaje Pre-entrenado BERT:
El modelo utiliza un modelo BERT pre-entrenado. BERT es un modelo de lenguaje bidireccional que se entrena en grandes cantidades de texto. Su característica distintiva es que procesa el texto en ambas direcciones (izquierda a derecha y derecha a izquierda) y captura relaciones contextuales de las palabras en un contexto más amplio.

#### Tokenizador: AutoTokenizer
El tokenizador se utiliza para dividir el texto en unidades más pequeñas llamadas tokens y mapear esas unidades a identificadores únicos. El tokenizador es una parte esencial del procesamiento de texto en modelos de lenguaje, y AutoTokenizer se encarga de cargar un tokenizador específico del modelo BERT.

#### Generación de Predicciones:
El programa utiliza el modelo BERT para predecir palabras o frases que deben reemplazar [MASK] en el texto de entrada. Las predicciones se generan extrayendo los tokens principales con las puntuaciones más altas de una capa específica del modelo. El número de predicciones a generar se controla mediante la constante K.

#### Rendimento del nivel de Atención:
El programa visualiza la atención del modelo en forma de diagramas para entender qué palabras o tokens tienen una atención más alta en función de la posición de [MASK]. Estos diagramas muestran cómo el modelo considera la relación entre palabras en un contexto. Los diagramas se generan en función de la salida de atención del modelo.
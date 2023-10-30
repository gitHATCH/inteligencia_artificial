# **Detección de Señales de Tráfico**
Este programa, traffic.py, es una aplicación de aprendizaje automático que se utiliza para identificar señales de tráfico en imágenes. Utiliza las librerías OpenCV y TensorFlow para cargar datos, crear un modelo de red neuronal convolucional (CNN) y entrenar el modelo para clasificar señales de tráfico en categorías específicas.

## Uso
El programa traffic.py se utiliza de la siguiente manera: <br>

```console
python traffic.py data_directory [model.h5] 
```
##### data_directory: 
Ruta al directorio que contiene las imágenes de señales de tráfico. <br>
##### [model.h5] (opcional): 
Ruta para guardar el modelo entrenado en un archivo h5.

## Funcionamiento
El programa se divide en varias secciones y métodos que desempeñan un papel fundamental en el proceso de identificación de señales de tráfico:

#### load_data: 
Se utiliza para cargar las imágenes de señales de tráfico y sus etiquetas. El programa espera que las imágenes estén organizadas en subdirectorios, donde el nombre del subdirectorio representa la categoría de la señal de tráfico. Las imágenes se redimensionan a un tamaño específico (definido por IMG_WIDTH y IMG_HEIGHT) antes de cargarlas. Este método devuelve dos listas: una lista de imágenes y una lista de etiquetas.

#### get_model:
Crea un modelo de red neuronal convolucional (CNN) utilizando la biblioteca TensorFlow. El modelo se compone de capas convolucionales, capas de max pooling y capas completamente conectadas. El número de categorías de señales de tráfico se define como NUM_CATEGORIES. El modelo se compila con una función de pérdida de entropía cruzada categórica y un optimizador Adam.

## Entrenamiento del Modelo:
El programa divide los datos en conjuntos de entrenamiento y prueba utilizando la función train_test_split de scikit-learn. A continuación, el modelo se entrena en el conjunto de entrenamiento utilizando el método fit. El número de épocas de entrenamiento se controla mediante la variable EPOCHS.

## Evaluación del Modelo:
El modelo se evalúa en el conjunto de prueba utilizando el método evaluate. Esto proporciona métricas de rendimiento, como la precisión de clasificación.

## Guardar el Modelo:
Si se proporciona un nombre de archivo como segundo argumento al programa, el modelo se guarda en un archivo h5 utilizando el método save de TensorFlow.

## Importancia de OpenCV y TensorFlow:
OpenCV (Open Source Computer Vision Library): OpenCV se utiliza para cargar imágenes, redimensionarlas y realizar diversas operaciones de procesamiento de imágenes. Es especialmente útil para preparar los datos antes de alimentarlos al modelo de TensorFlow. <br>

TensorFlow: TensorFlow es una biblioteca de aprendizaje automático desarrollada por Google. En este proyecto, se utiliza para definir, compilar y entrenar el modelo de red neuronal. TensorFlow ofrece herramientas poderosas para la construcción y capacitación de modelos de aprendizaje automático.

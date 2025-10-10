Las redes neuronales son ==sistemas de inteligencia artificial inspirados en el cerebro humano que aprenden y resuelven problemas complejos a través de algoritmos de aprendizaje automático==. Consisten en [neuronas](https://www.google.com/search?sca_esv=44031a392adcfbd3&q=neuronas&sa=X&ved=2ahUKEwjM-tCGm5WQAxV0LEQIHWPUM54QxccNegQIHxAB&mstk=AUtExfDTdAav-JNm1Z4zujfDRQhBJhxN8UWz_mpR0dq02RqV_sbceFrdKewaEkI23AptXRhWWXnU3ukYnCfATktuVqGbgXwnw82LZBGJ4FThCUTYBHzPGd5lVjXP-clQ-aGN7WTjEOwZWDWUfvg3ID7mec0LjYJ8xnvv9pRvLaHvLQ4KrRWq_mP88tsKOme9eFz9_Hm-&csui=3) (nodos) interconectadas en una estructura de capas (entrada, ocultas y salida) que procesan datos para reconocer patrones, clasificar información y realizar predicciones. Su objetivo es mejorar continuamente a medida que procesan más datos, permitiendo tareas como el reconocimiento de imágenes, el procesamiento de lenguaje natural y la conducción autónoma.

![[Pasted image 20251008121855.png]] 


## Cómo funcionan las redes neuronales

Como ya hemos comentado, las redes neuronales son un tipo de algoritmo de aprendizaje automático que se inspira en el cerebro humano. Aunque pueden parecer complejas, las redes neuronales se componen de estructuras y componentes básicos que trabajan juntos para procesar información y producir una salida.

### Estructura y componentes básicos de una red neuronal

La estructura básica de una red neuronal consta de capas de neuronas interconectadas. La capa de entrada recibe los datos y los envía a través de la red, mientras que la capa de salida produce la salida final. Entre la capa de entrada y la capa de salida, hay una o más capas ocultas que procesan la información.

Cada neurona en la red neuronal está conectada a otras neuronas a través de conexiones que, al igual que en el mundo biológico, son conocidas como sinapsis. Cada sinapsis tiene un peso asociado que determina la fuerza de la conexión, y durante el proceso de entrenamiento, estos pesos se ajustan mediante el aprendizaje para mejorar la precisión y el resultado de la salida de la red.

### Funciones de activación y su importancia

Las funciones de activación son una parte fundamental de cómo funcionan las redes neuronales. Cada neurona en la red neuronal utiliza una función de activación para determinar su salida en función de la entrada que recibe.

Las funciones de activación pueden ser lineales o no lineales. Las funciones lineales simplemente multiplican la entrada por un peso y agregan un término de sesgo. Las funciones no lineales, por otro lado, son más complejas y permiten a la red modelar relaciones no lineales en los datos.

La elección de la función de activación puede tener un impacto significativo en la capacidad de la red para aprender y generalizar a nuevos datos. Algunas funciones de activación comunes incluyen la función sigmoide, la función ReLU y la función tangente hiperbólica.

#### **Función sigmoide**

Esta función que se expresa como `f(x) = 1 / (1 + exp(-x))` tiene una forma de “S” y su rango de salida está entre 0 y 1. Es utilizada normalmente a menudo en problemas de clasificación binaria, es decir, donde la salida debe ser 0 o 1.


![[Pasted image 20251008122256.png]]

#### **Función ReLU**

La función de activación ReLU (Rectified Linear Unit) es la función más utilizada en las redes neuronales modernas. Su forma matemática es `f(x) = max(0, x)`, lo que significa que la salida es 0 para valores negativos y lineal para valores positivos. La ventaja principal de esta función es que proporciona un valor cero verdadero para las entradas negativas, pero comportándose de manera similar a la lineal. Está siendo actualmente usada de manera habitual en el aprendizaje profundo, donde acelera el proceso de aprendizaje en los casos de aprendizaje representacional.

![[Pasted image 20251008122329.png]]

#### **Función tangente hiperbólica (O tanh)**

La función de activación tanh es similar a la función sigmoidal, pero su rango de salida está entre -1 y 1. Su forma matemática es `f(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))`. Esta función resulta adecuada en los casos de problemas de clasificación binaria y también para problemas de regresión donde las salidas pueden ser negativas.

![[Pasted image 20251008122405.png]]


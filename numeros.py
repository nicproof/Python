import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Cargar el conjunto de datos MNIST
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalizar los datos de entrada para escalar los valores de píxeles entre 0 y 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Crear el modelo de red neuronal
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Capa de entrada: aplanar la imagen
    keras.layers.Dense(128, activation='relu'),   # Capa oculta: 128 neuronas con función de activación ReLU
    keras.layers.Dropout(0.2),                   # Capa de dropout para reducir el sobreajuste
    keras.layers.Dense(10)                        # Capa de salida: 10 neuronas para 10 clases (números del 0 al 9)
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=5)

# Evaluar el modelo
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print("\nExactitud en el conjunto de prueba:", test_acc)

# Hacer predicciones
predictions = model.predict(test_images)

# Mostrar algunas predicciones y las imágenes correspondientes
num_show = 5
for i in range(num_show):
    plt.figure()
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.title(f"Predicción: {np.argmax(predictions[i])}, Etiqueta real: {test_labels[i]}")
    plt.show()
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Cargar el conjunto de datos MNIST
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalizar los datos de entrada para escalar los valores de píxeles entre 0 y 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Crear el modelo de red neuronal
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Capa de entrada: aplanar la imagen
    keras.layers.Dense(128, activation='relu'),   # Capa oculta: 128 neuronas con función de activación ReLU
    keras.layers.Dropout(0.2),                   # Capa de dropout para reducir el sobreajuste
    keras.layers.Dense(10)                        # Capa de salida: 10 neuronas para 10 clases (números del 0 al 9)
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=5)

# Evaluar el modelo
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print("\nExactitud en el conjunto de prueba:", test_acc)

# Hacer predicciones
predictions = model.predict(test_images)

# Mostrar algunas predicciones y las imágenes correspondientes
num_show = 5
for i in range(num_show):
    plt.figure()
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.title(f"Predicción: {np.argmax(predictions[i])}, Etiqueta real: {test_labels[i]}")
    plt.show()

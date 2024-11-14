import tensorflow as tf
import numpy as np

# Input data
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=np.float16)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=np.float16)

# Model definition
hidden1 = tf.keras.layers.Dense(units=3, input_shape=[1])
hidden2 = tf.keras.layers.Dense(units=3)
output = tf.keras.layers.Dense(units=1)
model = tf.keras.Sequential([hidden1, hidden2, output])

# Model compilation
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

# Model training
print("Starting training...")
history = model.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Model trained!")

# Making a prediction
print("Let's make a prediction!")
result = model.predict([89.0])
print("The result is " + str(result) + " fahrenheit")

# Viewing the internal variables of the model
print("Internal model variables")
print(hidden1.get_weights())
print(hidden2.get_weights())
print(output.get_weights())


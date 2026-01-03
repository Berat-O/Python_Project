import tensorflow as tf
from matplotlib import pyplot as plt

import numpy as np

# Input data
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=np.float32)
fahrenheit = (celsius*1.8) + 32


# Model definition
Input_layer = tf.keras.layers.Input((1,))
hidden1 = tf.keras.layers.Dense(units=2)   #Dense Layer With 2 units so as to not overfit the data
output = tf.keras.layers.Dense(units=1)
model = tf.keras.Sequential([Input_layer,hidden1, output])
# Model compilation
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

# Model training
epochs = 100
print("Starting training...")
history = model.fit(celsius, fahrenheit, epochs=epochs, verbose=False)
loss = history.history["loss"]
print("Model trained!")

# Making a prediction
print("Let's make a prediction!")
result = model.predict(np.array([89.0]))
print("The result is " + str(result) + " fahrenheit")
print(f"True value = {(89.0*1.8) +32}")

# Viewing the internal variables of the model
print("Internal model variables")
print(hidden1.get_weights())
# print(hidden2.get_weights())
print(output.get_weights())

# loss changes 
plt.figure(figsize = (10,10))
plt.subplot(1,2,1)
plt.plot(range(epochs),loss)
plt.xlabel("Epochs")
plt.ylabel("loss")
plt.title("losse over epochs")

# true values vs predicted values 
plt.subplot(1,2,2)
x_test = np.random.randint(0,100,[20,1])
y_test = (x_test*1.8) +32
y_pred = model.predict(x_test)

plt.scatter(x_test, y_test, color='blue', label='True Values')
plt.scatter(x_test, y_pred, color='red', label='Predicted Values')
plt.xlabel("True values")
plt.ylabel("predicted values")
plt.title("True values vs Predicted values")
plt.show()
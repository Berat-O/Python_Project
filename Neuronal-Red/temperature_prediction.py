import tensorflow as tf
import numpy as np

# Input data: Celsius to Fahrenheit conversion data
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=np.float16)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=np.float16)

def build_model():
    """Build a simple neural network model for temperature conversion."""
    # Model definition with two hidden layers and one output layer
    hidden1 = tf.keras.layers.Dense(units=3, input_shape=[1], activation="relu")
    hidden2 = tf.keras.layers.Dense(units=3, activation="relu")
    output = tf.keras.layers.Dense(units=1)  # Linear output for regression
    model = tf.keras.Sequential([hidden1, hidden2, output])

    # Model compilation
    model.compile(optimizer=tf.keras.optimizers.Adam(0.1),
                  loss='mean_squared_error')
    return model, hidden1, hidden2, output

def train_model(model, inputs, targets, epochs=1000):
    """Train the model on the provided inputs and targets."""
    print("Starting training...")
    history = model.fit(inputs, targets, epochs=epochs, verbose=False)
    print("Model trained!")
    return history

def make_prediction(model, value):
    """Make a prediction with the trained model."""
    print(f"Making a prediction for Celsius value: {value}")
    result = model.predict([value])
    print(f"The result is {result[0][0]:.2f} Fahrenheit")
    return result[0][0]

def view_model_weights(hidden1, hidden2, output):
    """Display weights for each layer in the model."""
    print("\nInternal model variables (weights and biases):")
    print("Hidden Layer 1 weights and biases:")
    print(hidden1.get_weights())
    print("\nHidden Layer 2 weights and biases:")
    print(hidden2.get_weights())
    print("\nOutput Layer weights and biases:")
    print(output.get_weights())

if __name__ == "__main__":
    # Build and train the model
    model, hidden1, hidden2, output = build_model()
    history = train_model(model, celsius, fahrenheit, epochs=1000)

    # Make a prediction
    fahrenheit_prediction = make_prediction(model, 89.0)

    # View the internal weights of the model
    view_model_weights(hidden1, hidden2, output)

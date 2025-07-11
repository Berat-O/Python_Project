import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Configuration parameters
LEARNING_RATE = 0.1
EPOCHS = 1000
HIDDEN_UNITS = [3, 3]

def prepare_data():
    """Prepare and validate temperature conversion data"""
    celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=np.float16)
    fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=np.float16)
    
    if len(celsius) != len(fahrenheit):
        raise ValueError("Input arrays must have the same length")
    
    return celsius, fahrenheit

def build_model(input_shape=[1]):
    """Construct the neural network model"""
    layers = [tf.keras.layers.Dense(units=units, input_shape=input_shape) 
             for units in HIDDEN_UNITS[:1]]
    
    layers.extend([tf.keras.layers.Dense(units=units) 
                  for units in HIDDEN_UNITS[1:]])
    
    layers.append(tf.keras.layers.Dense(units=1))
    
    return tf.keras.Sequential(layers)

def train_model(model, x, y):
    """Train the model with specified parameters"""
    model.compile(
        optimizer=tf.keras.optimizers.Adam(LEARNING_RATE),
        loss='mean_squared_error'
    )
    
    return model.fit(x, y, epochs=EPOCHS, verbose=False)

def plot_training_loss(history):
    """Plot training loss over epochs"""
    plt.figure(figsize=(10, 6))
    plt.plot(history.history['loss'])
    plt.title('Model Training Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.show()

def predict_temperature(model, celsius_value):
    """Predict fahrenheit from celsius using trained model"""
    prediction = model.predict([celsius_value], verbose=False)
    return float(prediction[0][0])

def main():
    # Data preparation
    celsius, fahrenheit = prepare_data()
    
    # Model construction
    model = build_model()
    
    # Model training
    print("Starting training...")
    history = train_model(model, celsius, fahrenheit)
    print("Model trained!")
    
    # Visualize training process
    plot_training_loss(history)
    
    # Make prediction
    test_value = 89.0
    result = predict_temperature(model, test_value)
    print(f"Prediction: {test_value}°C = {result:.2f}°F")
    
    # Display model weights
    print("\nInternal model weights:")
    for i, layer in enumerate(model.layers):
        print(f"\nLayer {i+1} weights:")
        print(layer.get_weights())

if __name__ == "__main__":
    main()

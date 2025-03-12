import numpy as np

# Fungsi aktivasi Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Data training untuk XOR
X = np.array([[0, 0], 
              [0, 1], 
              [1, 0], 
              [1, 1]])

# Target output XOR
y = np.array([[0], 
              [1], 
              [1], 
              [0]])

# Struktur jaringan (2 input, 2 hidden, 1 output)
layer_sizes = [2, 2, 1]
np.random.seed(42)  # Untuk hasil yang konsisten

# Dictionary untuk menyimpan bobot dan bias
parameters = {}

# Inisialisasi bobot dan bias dengan loop
for i in range(len(layer_sizes) - 1):
    parameters[f"W{i+1}"] = np.random.uniform(size=(layer_sizes[i], layer_sizes[i+1]))
    parameters[f"b{i+1}"] = np.random.uniform(size=(1, layer_sizes[i+1]))

# Hyperparameters
lr = 0.1
epochs = 10000

# Training dengan backpropagation
for epoch in range(epochs):
    # Forward pass
    A = {"A0": X}  # Input sebagai layer pertama
    for i in range(1, len(layer_sizes)):  # Iterasi untuk tiap layer
        Z = np.dot(A[f"A{i-1}"], parameters[f"W{i}"]) + parameters[f"b{i}"]
        A[f"A{i}"] = sigmoid(Z)  # Semua layer menggunakan sigmoid

    # Error
    error = y - A[f"A{len(layer_sizes)-1}"]

    # Backpropagation
    dA = error * sigmoid_derivative(A[f"A{len(layer_sizes)-1}"])  # Semua layer menggunakan sigmoid
    deltas = {f"dA{len(layer_sizes)-1}": dA}

    for i in range(len(layer_sizes)-2, 0, -1):  # Iterasi mundur untuk hidden layers
        dA = deltas[f"dA{i+1}"].dot(parameters[f"W{i+1}"].T) * sigmoid_derivative(A[f"A{i}"])
        deltas[f"dA{i}"] = dA

    # Update bobot dan bias
    for i in range(1, len(layer_sizes)):
        parameters[f"W{i}"] += A[f"A{i-1}"].T.dot(deltas[f"dA{i}"]) * lr
        parameters[f"b{i}"] += np.sum(deltas[f"dA{i}"], axis=0, keepdims=True) * lr

    # Menampilkan error setiap 1000 epoch
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {np.mean(np.abs(error))}")

# Tes hasil
print("\nHasil prediksi XOR setelah training:")
for i in range(len(X)):
    A_test = X[i]
    for j in range(1, len(layer_sizes)):  # Forward pass
        Z = np.dot(A_test, parameters[f"W{j}"]) + parameters[f"b{j}"]
        A_test = sigmoid(Z)  # Semua layer menggunakan sigmoid
    print(f"Input: {X[i]}, Output: {A_test.round()}")  # Dibulatkan ke 0 atau 1

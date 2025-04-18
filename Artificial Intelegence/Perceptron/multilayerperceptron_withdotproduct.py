import numpy as np

# ==== Utility Function ====
def relu(z):
    return np.maximum(0, z)

def relu_derivative(z):
    return (z > 0).astype(float)

def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=0, keepdims=True))
    return exp_z / np.sum(exp_z, axis=0, keepdims=True)

def cross_entropy_loss(y_true, y_pred):
    return -np.sum(y_true * np.log(y_pred + 1e-9)) / y_true.shape[1]

def one_hot(labels, num_classes):
    return np.eye(num_classes)[labels].T  # shape: (num_classes, batch_size)

# ==== Network Dimensions ====
n_input = 4
n_hidden1 = 8
n_hidden2 = 6
n_hidden3 = 5
n_output = 3

# ==== Hyperparameters ====
learning_rate = 0.01
epochs = 1000
batch_size = 5
num_samples = 100

# ==== Generate Dummy Dataset ====
X = np.random.rand(n_input, num_samples)             # shape: (4, 100)
y_labels = np.random.randint(0, n_output, num_samples)
Y = one_hot(y_labels, n_output)                      # shape: (3, 100)

# ==== Initialize Weights and Biases ====
def init_weights(shape):
    return np.random.randn(*shape) * 0.1

W1 = init_weights((n_hidden1, n_input))
b1 = np.zeros((n_hidden1, 1))

W2 = init_weights((n_hidden2, n_hidden1))
b2 = np.zeros((n_hidden2, 1))

W3 = init_weights((n_hidden3, n_hidden2))
b3 = np.zeros((n_hidden3, 1))

W4 = init_weights((n_output, n_hidden3))
b4 = np.zeros((n_output, 1))

# ==== Training Loop ====
for epoch in range(epochs):
    permutation = np.random.permutation(num_samples)
    X_shuffled = X[:, permutation]
    Y_shuffled = Y[:, permutation]

    for i in range(0, num_samples, batch_size):
        X_batch = X_shuffled[:, i:i + batch_size]  # shape: (4, batch_size)
        Y_batch = Y_shuffled[:, i:i + batch_size]  # shape: (3, batch_size)

        # === Forward Pass ===
        z1 = np.dot(W1, X_batch) + b1
        a1 = relu(z1)

        z2 = np.dot(W2, a1) + b2
        a2 = relu(z2)

        z3 = np.dot(W3, a2) + b3
        a3 = relu(z3)

        z4 = np.dot(W4, a3) + b4
        a4 = softmax(z4)

        # === Backward Pass ===
        dz4 = a4 - Y_batch
        dW4 = np.dot(dz4, a3.T) / batch_size
        db4 = np.sum(dz4, axis=1, keepdims=True) / batch_size

        da3 = np.dot(W4.T, dz4)
        dz3 = da3 * relu_derivative(z3)
        dW3 = np.dot(dz3, a2.T) / batch_size
        db3 = np.sum(dz3, axis=1, keepdims=True) / batch_size

        da2 = np.dot(W3.T, dz3)
        dz2 = da2 * relu_derivative(z2)
        dW2 = np.dot(dz2, a1.T) / batch_size
        db2 = np.sum(dz2, axis=1, keepdims=True) / batch_size

        da1 = np.dot(W2.T, dz2)
        dz1 = da1 * relu_derivative(z1)
        dW1 = np.dot(dz1, X_batch.T) / batch_size
        db1 = np.sum(dz1, axis=1, keepdims=True) / batch_size

        # === Update Parameters ===
        W4 -= learning_rate * dW4
        b4 -= learning_rate * db4

        W3 -= learning_rate * dW3
        b3 -= learning_rate * db3

        W2 -= learning_rate * dW2
        b2 -= learning_rate * db2

        W1 -= learning_rate * dW1
        b1 -= learning_rate * db1

    # === Logging Loss per Epoch ===
    if (epoch + 1) % 100 == 0 or epoch == 0:
        pred_all = softmax(np.dot(W4, relu(np.dot(W3, relu(np.dot(W2, relu(np.dot(W1, X) + b1)) + b2)) + b3)) + b4)
        loss = cross_entropy_loss(Y, pred_all)
        acc = np.mean(np.argmax(pred_all, axis=0) == y_labels)
        print(f"Epoch {epoch + 1}/{epochs} - Loss: {loss:.4f} - Acc: {acc:.2%}")

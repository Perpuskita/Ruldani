import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"


import numpy as np
from keras.api.datasets import mnist
from keras.api.utils import to_categorical

# ======== FUNGSI AKTIVASI & LOSS ========
def tanh(x): return np.tanh(x)
def tanh_derivative(x): return 1 - np.tanh(x) ** 2
def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
def cross_entropy(y_true, y_pred):
    return -np.sum(y_true * np.log(y_pred + 1e-8), axis=-1).mean()

# ======== KONVOLUSI & BACKPROP ========
def conv2d(x, kernels):
    batch_size, x_h, x_w = x.shape
    num_kernels, k_h, k_w = kernels.shape
    output_h, output_w = x_h - k_h + 1, x_w - k_w + 1
    output = np.zeros((batch_size, num_kernels, output_h, output_w))
    for i in range(output_h):
        for j in range(output_w):
            output[:, :, i, j] = np.sum(x[:, np.newaxis, i:i+k_h, j:j+k_w] * kernels, axis=(2, 3, 4))
    return output

def conv2d_backprop(d_out, x, kernels, learning_rate):
    batch_size, x_h, x_w = x.shape
    num_kernels, k_h, k_w = kernels.shape
    d_kernels = np.zeros_like(kernels)
    for i in range(d_out.shape[2]):
        for j in range(d_out.shape[3]):
            d_kernels += np.sum(d_out[:, :, i, j][:, :, np.newaxis, np.newaxis] * x[:, np.newaxis, i:i+k_h, j:j+k_w], axis=0)
    kernels -= learning_rate * d_kernels / batch_size
    return kernels

# ======== POOLING ========
def avg_pooling(x, size=2, stride=2):
    batch_size, channels, x_h, x_w = x.shape
    output_h = (x_h - size) // stride + 1
    output_w = (x_w - size) // stride + 1
    output = np.zeros((batch_size, channels, output_h, output_w))
    for i in range(0, x_h - size + 1, stride):
        for j in range(0, x_w - size + 1, stride):
            output[:, :, i // stride, j // stride] = np.mean(x[:, :, i:i+size, j:j+size], axis=(2, 3))
    return output

def avg_pooling_backprop(d_out, x, size=2, stride=2):
    d_x = np.zeros_like(x)
    for i in range(0, x.shape[2] - size + 1, stride):
        for j in range(0, x.shape[3] - size + 1, stride):
            d_x[:, :, i:i+size, j:j+size] += d_out[:, :, i // stride, j // stride][:, :, np.newaxis, np.newaxis] / (size * size)
    return d_x

# ======== LOAD MNIST ========
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = np.pad(x_train, ((0, 0), (2, 2), (2, 2)), mode='constant') / 255.0  # Resize ke 32x32 & normalisasi
x_test = np.pad(x_test, ((0, 0), (2, 2), (2, 2)), mode='constant') / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# ======== INISIALISASI BOBOT ========
def init_weights(shape): return np.random.randn(*shape) * 0.1
batch_size = 32
learning_rate = 0.01
conv1_kernels = init_weights((6, 5, 5))
fc1_weights = init_weights((150, 84))
fc1_bias = np.zeros(84)
fc2_weights = init_weights((84, 10))
fc2_bias = np.zeros(10)

# ======== TRAINING LOOP ========
epochs = 5
for epoch in range(epochs):
    for i in range(0, len(x_train), batch_size):
        input_images = x_train[i:i+batch_size]
        y_true = y_train[i:i+batch_size]

        # **FORWARD PASS**
        conv1_output = tanh(conv2d(input_images, conv1_kernels))  
        pool1_output = avg_pooling(conv1_output)  
        flatten_output = pool1_output.reshape(batch_size, -1)  
        fc1_output = tanh(flatten_output @ fc1_weights + fc1_bias)  
        fc2_output = softmax(fc1_output @ fc2_weights + fc2_bias)  

        # **Loss**
        loss = cross_entropy(y_true, fc2_output)

        # **BACKPROPAGATION**
        d_fc2 = (fc2_output - y_true) / batch_size
        d_fc2_weights = fc1_output.T @ d_fc2
        d_fc2_bias = np.sum(d_fc2, axis=0)
        d_fc1 = d_fc2 @ fc2_weights.T * tanh_derivative(fc1_output)
        d_fc1_weights = flatten_output.T @ d_fc1
        d_fc1_bias = np.sum(d_fc1, axis=0)
        d_flatten = d_fc1 @ fc1_weights.T
        d_pool1 = d_flatten.reshape(pool1_output.shape)
        d_conv1 = avg_pooling_backprop(d_pool1, conv1_output)
        conv1_kernels = conv2d_backprop(d_conv1, input_images, conv1_kernels, learning_rate)

        # **Update Weights**
        fc2_weights -= learning_rate * d_fc2_weights
        fc2_bias -= learning_rate * d_fc2_bias
        fc1_weights -= learning_rate * d_fc1_weights
        fc1_bias -= learning_rate * d_fc1_bias

    print(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}")

# ======== TESTING ========
correct = 0
for i in range(0, len(x_test), batch_size):
    input_images = x_test[i:i+batch_size]
    y_true = y_test[i:i+batch_size]
    conv1_output = tanh(conv2d(input_images, conv1_kernels))
    pool1_output = avg_pooling(conv1_output)
    flatten_output = pool1_output.reshape(batch_size, -1)
    fc1_output = tanh(flatten_output @ fc1_weights + fc1_bias)
    fc2_output = softmax(fc1_output @ fc2_weights + fc2_bias)
    correct += np.sum(np.argmax(fc2_output, axis=-1) == np.argmax(y_true, axis=-1))

accuracy = correct / len(x_test)
print(f"Test Accuracy: {accuracy:.4f}")

import numpy as np

# Mean Squared Error (MSE) sebagai contoh loss function
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Gradien dari MSE
def mse_gradient(y_true, y_pred):
    return -2 * (y_true - y_pred) / len(y_true)

# Optimizer Adam (Implementasi manual)
def adam_optimizer(grad, m, v, t, lr=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8):
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * (grad ** 2)

    # Bias correction
    m_hat = m / (1 - beta1 ** t)
    v_hat = v / (1 - beta2 ** t)

    # Parameter update
    update = lr * m_hat / (np.sqrt(v_hat) + epsilon)
    return update, m, v

# Contoh penggunaan
y_true = np.array([1.0, 2.0, 3.0])
y_pred = np.array([0.9, 1.8, 3.1])

# Inisialisasi Adam
m, v, t = 0, 0, 1

# Hitung loss
loss = mse_loss(y_true, y_pred)
grad = mse_gradient(y_true, y_pred)

# Update parameter menggunakan Adam
update, m, v = adam_optimizer(grad, m, v, t)

print("Loss:", loss)
print("Gradien:", grad)
print("Update Parameter:", update)

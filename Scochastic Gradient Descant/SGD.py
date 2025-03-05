import numpy as np
from functools import reduce

# Data contoh (X sebagai input, y sebagai target)
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Inisialisasi parameter
w = np.random.randn()  # Bobot awal
b = np.random.randn()  # Bias awal
learning_rate = 0.01
epochs = 1000

# Fungsi loss (Mean Squared Error)
mse_loss = lambda w, b: np.mean((y - (w * X + b)) ** 2)

# Fungsi gradien secara fungsional
grad_w = lambda w, b, x, y: -2 * x * (y - (w * x + b))
grad_b = lambda w, b, x, y: -2 * (y - (w * x + b))

# Fungsi untuk update parameter dengan SGD
update_params = lambda params, sample: (
    params[0] - learning_rate * grad_w(params[0], params[1], sample[0], sample[1]),
    params[1] - learning_rate * grad_b(params[0], params[1], sample[0], sample[1])
)

# Training loop menggunakan reduce untuk iterasi
for _ in range(epochs):
    # Ambil satu sampel secara acak untuk stochastic update
    idx = np.random.randint(len(X))
    sample = (X[idx], y[idx])

    # Update parameter menggunakan reduce
    w, b = reduce(update_params, [sample], (w, b))

# Hasil akhir setelah training
print(f"Final Weights: w = {w}, b = {b}")
print(f"Final Loss: {mse_loss(w, b)}")

import numpy as np
import matplotlib.pyplot as plt

# Definisikan fungsi f(x)
def turunan_f(x):
    return 30 * x * (3 * x**2 + 2)**4

def f(x):
    return (3*x**2+2)**5

# Rentang nilai x
x = np.linspace(-3, 3, 400)

# Plot grafik
plt.figure(figsize=(8, 5))
plt.plot(x, turunan_f(x), label='turunan f(x)', color='blue')
plt.plot(x, f(x), label='f(x)', color='red')
# Tambahkan grid, label, dan judul
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.title("Grafik Fungsi f(x) = 30x(3x² + 2)^4")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()

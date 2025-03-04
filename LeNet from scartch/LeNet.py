import numpy as np
import matplotlib.pyplot as plt

# Load Dataset Mnist

dir = "mnist/"

x_test = np.load(dir+"x_test.npy")  # x_test
x_train = np.load(dir+"x_train.npy")  # x_train

y_test = np.load(dir+"/y_test.npy")  # y_test
y_train = np.load(dir+"/y_train.npy")  # y_train

# Change Format Dataset Mnist

x_test = x_test.astype('float32') / 255.0
x_train = x_train.astype('float32') / 255.0

y_test = x_test.astype('float32') / 255.0
y_train = x_train.astype('float32') / 255.0

# Def function

def tanh(x)-> float:
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def softmax(x)-> float:
    # Mengurangi nilai maksimum dari x untuk stabilitas numerik
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def create_kernel(x,y):
    return np.random.rand(5, 5)

def Layer_Conv2D(kernel_size, activation, stride = 1, padding = 1):
    print("layer2d")

def Layer_Pool_Maxpooling(kernel_size, stride = 1, padding = 1):
    print("Layer_Pool")

def Fully_Connected():
    print("Fully_Connected")

def Back_Propagation():
    print("Back_Propagation")

# Def arsitecture

def Arsitecture_LeNet():
    Model_Sequential = Layer_Conv2D(1,1)

Arsitecture_LeNet()
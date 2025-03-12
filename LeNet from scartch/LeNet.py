import numpy as np
import matplotlib.pyplot as plt

# Def function

def tanh(x)-> float:
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def softmax(x)-> float:

    # Mengurangi nilai maksimum dari x untuk stabilitas numerik
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def create_layer(size):
    print(size)

def Back_Propagation():
    print("Back_Propagation")

def Layer_Conv2D(kernel = (1,1), channel = 1, layer = 1, stride = 0, padding = 0, type = "Relu"):
    return np.random.rand(*((channel, layer) + kernel))

def Layer_Pool(kernel = (1,1), type = "Max Pool", stride = 0, padding = 0):
    return np.random.rand(*kernel)

def Layer_Fully_Connected():
    print("Fully_Connected")

def Model_Sequential( model ):
    # print ("Model Sequential")
    return model

def Layer_Flatten( ):
    print("Layer Flatten")

def Compile( model ):
    print("model compile")
    return model

def fit( model ):
    print("fit")

# Def arsitecture : https://www.geeksforgeeks.org/lenet-5-architecture/

model = Model_Sequential([
    Layer_Conv2D(),
    Layer_Pool(),
    Layer_Conv2D(),
    Layer_Pool(),
    Layer_Flatten(),
    Layer_Fully_Connected(),
    Layer_Fully_Connected(),
    Layer_Fully_Connected()
])

model = Compile(model)
print(model)
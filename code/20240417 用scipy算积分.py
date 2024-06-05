import numpy as np
from scipy.integrate import quad
import math

# Define the function to integrate
def f(x):
    return np.exp(-x**2)

# Specify the limits of integration
a = 0
b = 1

# Compute the definite integral
result, error = quad(f, a, b)

print("Integral result:", result)
print("Estimated error:", error)
import numpy as np

# Gradient Descent function


def gradient_descent(f_prime, x0, lr=0.01, iterations=10000, tolerance=1e-6):
    x = x0
    for i in range(iterations):
        grad = f_prime(x)
        x_new = x - lr * grad
        if abs(x_new - x) < tolerance:
            break
        x = x_new
    return x

# Function 1: y = 3(x-5)^4 + 8(x-5)^3 - 18(x-5)^2


def f1_prime(x):
    return 12*(x-5)**3 + 24*(x-5)**2 - 36*(x-5)

# Function 2: y = 6x^3 - 12x^2 + 1


def f2_prime(x):
    return 18*x**2 - 24*x

# Function 3: y = 4x / (1 + x^2)


def f3_prime(x):
    return (4 - 4*x**2) / (1 + x**2)**2

# Function 4: y = 4*sqrt(x) - x^2


def f4_prime(x):
    return 2/np.sqrt(x) - 2*x


# Initial guesses
x0_list = [6, 0.5, 1, 1]

# Apply Gradient Descent
min1 = gradient_descent(f1_prime, x0_list[0], lr=0.01)
min2 = gradient_descent(f2_prime, x0_list[1], lr=0.01)
# may find max/min depending on start
min3 = gradient_descent(f3_prime, x0_list[2], lr=0.01)
min4 = gradient_descent(f4_prime, x0_list[3], lr=0.01)  # maximum

print("Function 1 minimum at x =", min1)
print("Function 2 minimum at x =", min2)
print("Function 3 extremum at x =", min3)
print("Function 4 maximum at x =", min4)

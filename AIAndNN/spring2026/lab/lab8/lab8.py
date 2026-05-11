import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Data load karne aur pre-process karne ka function


def load_data():
    # Iris dataset ka URL
    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    data = pd.read_csv(URL, header=None)

    # Dataset ko linearly separable banane ke liye pehle 100 samples select kiye
    data = data[:100]

    # 'Iris-setosa' ko 0 aur 'Iris-versicolor' ko 1 mein convert kiya
    data[4] = np.where(data.iloc[:, -1] == 'Iris-setosa', 0, 1)

    # Data ko matrix form mein convert kiya
    data = np.asmatrix(data, dtype='float64')
    return data

# 2. Perceptron Algorithm ki implementation


def perceptron(data, num_iter):
    # Features aur Labels ko alag kiya
    features = data[:, :-1]
    labels = data[:, -1]

    # Weights ko zero se initialize kiya (5 weights: 4 features + 1 bias)
    w = np.zeros(shape=(1, features.shape[1] + 1))

    misclassified_ = []

    for epoch in range(num_iter):
        misclassified = 0
        for x, label in zip(features, labels):
            # Bias term ke liye 1 insert kiya
            x_with_bias = np.insert(x, 0, 1)

            # Dot product calculate kiya
            y_val = np.dot(w, x_with_bias.transpose())

            # Hardlimiter activation function (0 ya 1)
            target = 1.0 if (y_val > 0) else 0.0

            # Error (delta) calculate kiya
            delta = label.item(0, 0) - target

            # Agar misclassification hai to weights update karein
            if (delta):
                misclassified += 1
                w += (delta * x_with_bias)

        misclassified_.append(misclassified)

    return w, misclassified_

# --- Code ko Run karein ---


# Data load karein
data = load_data()

plt.scatter(np.array(data[:50,0]), np.array(data[:50,2]), marker='o', label='setosa')
plt.scatter(np.array(data[50:,0]), np.array(data[50:,2]), marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend()
plt.show()


# Hyperparameter: Iterations ki tadaad
num_iter = 10

# Model ko train karein
weights, errors = perceptron(data, num_iter)

# Results print karein
print("Final Weights:", weights)
print("Errors per iteration:", errors)

# Misclassifications ka graph plot karein (Lab Task ke liye)
plt.plot(range(1, num_iter + 1), errors, marker='o')
plt.xlabel('Iterations (Epochs)')
plt.ylabel('Number of misclassifications')
plt.title('Perceptron Learning Convergence')
plt.grid()
plt.show()

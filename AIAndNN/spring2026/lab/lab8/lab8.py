import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- SECTION 1: DATA PREPARATION ---
# Theory: Dataset ko numerical matrix mein badalna taake dot product ho sake.


def load_data():
    # 1. Iris dataset ka raw data UCI repository se load ho raha hai
    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    data = pd.read_csv(URL, header=None)
    # print("Raw Data Sample:\n", data)
    # 2. Linear Separability: Perceptron sirf linearly separable data solve karta hai,
    # isliye humne sirf pehle 2 classes (Setosa & Versicolor) select ki hain.
    data = data[:100]
    # print("Filtered Data Sample (Setosa & Versicolor):\n", data)
    # 3. Encoding: Theory mein target labels numerical (0 aur 1) hone chahiye.
    # Jahan 'Iris-setosa' hai wahan 0, warna 1 set kar diya.
    data[4] = np.where(data.iloc[:, -1] == 'Iris-setosa', 0, 1)
    # print("Encoded Data Sample:\n", data)


    # 4. Conversion: Dataframe ko Numpy Matrix mein badla taake mathematical operations fast hon.
    data = np.asmatrix(data, dtype='float64')
    return data

# --- SECTION 2: PERCEPTRON ALGORITHM ---
# Theory Formula: y = f( Σ (w_i * x_i) + b )


def perceptron(data, num_iter):
    # 1. Slicing: Columns 0-3 features hain (x), Column 4 label hai (y).
    features = data[:, :-1]
    labels = data[:, -1]
    print("Features Sample:\n", features[:5])
    print("Labels Sample:\n", labels[:5])
    # 2. Initialization: Weights ko 0 set kiya.
    # Shape (1, 5) kyunke 4 features hain aur 1 Bias (w0) hai.
    w = np.zeros(shape=(1, features.shape[1] + 1))
    print("Initial Weights Shape:", w.shape)

    print("Initial Weights:", w)
    misclassified_ = []  # Har epoch ki galtiyan track karne ke liye list

    # 3. Outer Loop (Epochs): Pura dataset bar-bar dikhane ke liye revision loop.
    for epoch in range(num_iter):
        misclassified = 0

        # 4. Inner Loop (Training): Har ek phool (sample) par bari-bari jana.
        for x, label in zip(features, labels):
            # print(f"\nEpoch {epoch+1}, Sample: {x}, Label: {label}")
            # Theory: Bias term 'b' ko vector calculation mein lane ke liye Input mein '1' add kiya.
            # Equation: x = [1, x1, x2, x3, x4]
            x_with_bias = np.insert(x, 0, 1)

            # Theory Calculation: Dot Product (Z = w . x)
            # Ye Summation Σ operation hai: w0*1 + w1*x1 + w2*x2...
            y_val = np.dot(w, x_with_bias.transpose())

            # Theory: Activation Function (Hardlimiter / Step Function)
            # Prediction (target) = 1 if z > 0 else 0
            target = 1.0 if (y_val > 0) else 0.0

            # Theory: Delta Calculation (Error = Actual - Predicted)
            # label.item() matrix se scalar value nikalne ke liye hai.
            delta = label.item(0, 0) - target

            # Theory: Weight Update Rule (Learning)
            # Formula: w_new = w_old + (Learning_Rate * Delta * x)
            # Note: Is code mein learning rate 1 hai.
            if (delta):
                misclassified += 1  # Agar galti hai to counter barhao
                # print(f"Updating Weights. Delta: {delta}")
                # Weight update sirf galti par hota hai
                print(f"Before Update: {w}")
                # print(f"Input with Bias: {x_with_bias}")
                w += (delta * x_with_bias)
                print(f"After Update: {w}")

        # Epoch ke end par total galtiyan save karein
        misclassified_.append(misclassified)

    return w, misclassified_

# --- SECTION 3: EXECUTION & VISUALIZATION ---


# Data load kiya
data = load_data()
# print("Data Loaded. Sample:\n", data)

# # Scatter Plot: Visualizing the features (Petal vs Sepal)
# plt.scatter(np.array(data[:50, 0]), np.array(
#     data[:50, 2]), marker='o', label='setosa')
# plt.scatter(np.array(data[50:, 0]), np.array(
#     data[50:, 2]), marker='x', label='versicolor')
# plt.xlabel('petal length')
# plt.ylabel('sepal length')
# plt.legend()
# plt.show()

# Training: Model 10 baar dataset ko dekh kar weights adjust karega
num_iter = 10
weights, errors = perceptron(data, num_iter)

print("Final Weights:", weights)
print("Errors per iteration:", errors)


# # --- SECTION 4: FINAL EQUATION PRINTING ---

# Hum weights matrix se values nikal rahe hain
b = weights[0, 0]   # Pehla weight hamara Bias hai
w1, w2, w3, w4 = weights[0, 1], weights[0, 2], weights[0, 3], weights[0, 4]

print("\n" + "="*30)
print("🎯 FINAL DECISION BOUNDARY")
print("="*30)
# Equation format: z = w1*x1 + w2*x2 + w3*x3 + w4*x4 + b
print(f"z = ({w1:.2f})*PetalLen + ({w2:.2f})*PetalWid + ({w3:.2f})*SepalLen + ({w4:.2f})*SepalWid + ({b:.2f})")
print("Rule: If z > 0, then 'Versicolor', else 'Setosa'")
print("="*30)

# Convergence Graph: Ye graph dikhata hai ke galti kaise zero ki taraf ja rahi hai.
plt.plot(range(1, num_iter + 1), errors, marker='o')
plt.xlabel('Iterations (Epochs)')
plt.ylabel('Number of misclassifications')
plt.title('Perceptron Learning Convergence')
plt.grid()
plt.show()

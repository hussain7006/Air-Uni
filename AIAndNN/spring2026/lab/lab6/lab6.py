import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

# 1. Dataset Taiyar Karein (Jo humne HTML mein dekha)
# Columns: [Bias, Size, Bedrooms, Floors, Age]
data = {
    'Size': [2104, 1416, 1534, 852, 3000],
    'Bedrooms': [5, 3, 3, 2, 4],
    'Floors': [1, 2, 2, 1, 1],
    'Age': [45, 40, 30, 36, 38],
    'Price': [460, 232, 315, 178, 540]
}

df = pd.DataFrame(data)

print("--- Dataset ---")
print(df)


# 2. X aur y Matrices Banayen
X = df[['Size', 'Bedrooms', 'Floors', 'Age']].values
y = df['Price'].values.reshape(-1, 1)

# print("\n--- Feature Matrix (X) ---")
# print(X)

# print("\n--- Target Vector (y) ---")
# print(y)

# print("\n--- Shapes ---")
# print(f"X shape: {X.shape[0]} ")
# print(np.ones((X.shape[0], 1))) 

# 3. Bias Column (All 1s) add karein (Matrix multiplication ke liye lazmi hai)
ones = np.ones((X.shape[0], 1)) # Bias column ke liye ek column of ones banayen
X_bias = np.append(ones, X, axis=1) # Bias column add karna zaroori hai taake intercept ko bhi calculate kiya ja sake

print("\n--- Feature Matrix with Bias (X_bias) ---")
# print(X_bias)

# 4. NORMAL EQUATION (theta = (X^T * X)^-1 * X^T * y)
print("--- Step 1: Transposing & Multiplying ---")
XT_X = np.matmul(X_bias.T, X_bias)

print("--- Step 2: Calculating Inverse ---")
XT_X_inv = np.linalg.inv(XT_X)

# print('inverse of X^T * X:')
# print(XT_X_inv)

print("--- Step 3: Final Multiplication with y ---")
theta = np.dot(np.dot(XT_X_inv, X_bias.T), y)



# 5. Output Results
print("\n--- Final Weights (Theta) ---")
labels = ['Intercept (Bias)', 'Size', 'Bedrooms', 'Floors', 'Age']
for i in range(len(labels)):
    print(f"{labels[i]}: {theta[i][0]:.4f}")

# 6. Prediction Function

eqn = "Price = (Intercept) + (Size * Size Coefficient) + (Bedrooms * Bedrooms Coefficient) + (Floors * Floors Coefficient) + (Age * Age Coefficient)"
print(f"\n--- Linear Regression Equation ---\n{eqn}")

intercept = theta[0][0]

def predict_price(size, beds, floors, age):
    features = np.array([1, size, beds, floors, age])
    prediction = np.dot(features, theta)
    return prediction[0]


# Check Prediction
sample_price = predict_price(1800, 3, 1, 20)
print(f"\nPredicted Price for 1800sqft house: ${sample_price:.2f}k")

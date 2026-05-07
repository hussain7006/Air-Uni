import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Load data from CSV file (Iris dataset)
# Replace 'Iris.csv' with your actual CSV file path if needed
df = pd.read_csv('Iris.csv')

print(df)

# Convert the dataframe to a NumPy array
df1 = df.to_numpy()

print("df1:", df1)

# Select columns 1 to 4 (SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm) as features
# Skip the 'Id' column (index 0) and the header row.
X = df1[:, 1:5] # Start from the second row (index 1) to exclude the header

print("X:", X)


pca = PCA(n_components=3) # PCA object banate hain jisme hum 2 components chahte hain
transformed_data = pca.fit_transform(X)
print("Transformed Data:", transformed_data)


























# # ---------------------------------------------------------
# # STEP 1: Data Load Karna
# # ---------------------------------------------------------
# # Agar file local computer par hai to:
# df = pd.read_csv('Iris.csv')

# # Features select karna (Sepal/Petal lengths & widths)
# # Hum ID aur Species columns ko drop kar rahe hain features ke liye
# X = df.drop(['Id', 'Species'], axis=1)
# y = df['Species'] # Target classes

# # ---------------------------------------------------------
# # STEP 2: Standardization (Bohat Zaroori!)
# # ---------------------------------------------------------
# # PCA variance dekhta hai, is liye scales ka barabar hona zaroori hai
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# print(f"Original Data Shape: {X.shape}") # (150, 4)

# # ---------------------------------------------------------
# # STEP 3: Task - PCA with 2 Components
# # ---------------------------------------------------------
# pca_2d = PCA(n_components=2)
# X_pca_2d = pca_2d.fit_transform(X_scaled)

# print(f"Transformed Data Shape (2D): {X_pca_2d.shape}") # (150, 2)

# # Scatter Plot (Original data ki classes ko visualize karna)
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x=X_pca_2d[:, 0], y=X_pca_2d[:, 1], hue=y, palette='viridis')
# plt.title('PCA: Iris Dataset (2 Components)')
# plt.xlabel('Principal Component 1 (PC1)')
# plt.ylabel('Principal Component 2 (PC2)')
# plt.grid(True)
# plt.show()

# # ---------------------------------------------------------
# # STEP 4: Task - Eigenvalues aur Eigenvectors
# # ---------------------------------------------------------
# # Matrix A jo lab task mein di gayi hain
# A1 = np.array([[2, 3, 3], [2, 2, -3], [4, -3.1, 2]])
# A2 = np.array([[2, 3, 3], [2, 2, 3], [4, 3.1, 7]])

# def check_eig(matrix, name):
#     values, vectors = np.linalg.eig(matrix)
#     print(f"\n--- Matrix {name} ---")
#     print(f"Eigenvalues: {values}")
#     print(f"Eigenvectors:\n{vectors}")

# check_eig(A1, "A1")
# check_eig(A2, "A2")

# # ---------------------------------------------------------
# # STEP 5: Task - 95% Variance Challenge
# # ---------------------------------------------------------
# # Hum chahte hain ke itne components hon jo 95% info save rakhein
# pca_95 = PCA(n_components=0.95)
# X_pca_95 = pca_95.fit_transform(X_scaled)

# print("\n--- 95% Variance Task ---")
# print(f"Components needed for 95% variance: {pca_95.n_components_}")
# print(f"Explained Variance Ratio: {pca_95.explained_variance_ratio_}")

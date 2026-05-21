# ============================================================================
# AIR UNIVERSITY - DEPARTMENT OF MECHATRONICS ENGINEERING
# ARTIFICIAL INTELLIGENCE LAB 09/10: SVM GRAPHICAL VISUALIZATION
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# Load dataset 
cancer = datasets.load_breast_cancer()

# ----------------------------------------------------------------------------
# VISUALIZATION TASK: Plotting SVM Decision Boundary using first 2 features
# ----------------------------------------------------------------------------
# Hum sirf pehle 2 features le rahe hain taake 2D graph ban sake:
# Feature 0: 'mean radius', Feature 1: 'mean texture'
X = cancer.data[:, :2]  
y = cancer.target

# Split dataset (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=109)

# Train SVM Classifier with Linear Kernel
print("[INFO] Training SVM on 2 features for graphical plotting...")
clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(X_train, y_train)

# Predictions aur Accuracy nikalein
y_pred = clf.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"[INFO] 2-Feature Model Accuracy: {accuracy*100:.2f}%")

# --- GRAPH PLOTTING LOGIC ---
plt.figure(figsize=(10, 7))

# 1. Scatter Plot for Data Points (Train + Test combined for visual effect)
# Malignant (0) ko Red Stars aur Benign (1) ko Green Triangles se plot karte hain
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='#fb7185', marker='*', s=50, label='Malignant (Class 0)')
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='#4ade80', marker='^', s=40, label='Benign (Class 1)')

# 2. Hyperplane aur Margins Draw karna
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Grid create karein decision surface evaluate karne ke liye
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# Contour line draw karein (Z=0 hyperplane hai, Z=-1 aur Z=1 margins hain)
contours = ax.contour(XX, YY, Z, colors=['#4ade80', 'white', '#fb7185'], levels=[-1, 0, 1],
                      alpha=0.9, linestyles=['--', '-', '--'], linewidths=[1.5, 3.0, 1.5])

# Support Vectors ko highlight karna (Bigger hollow circles)
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
           linewidth=1.5, facecolors='none', edgecolors='white', label='Support Vectors')

# Styling and Labels (Air University Theme)
plt.title(f"Air University | SVM Decision Boundary (Accuracy: {accuracy*100:.2f}%)", 
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Feature 1: Mean Radius", fontsize=11, fontweight='semibold')
plt.ylabel("Feature 2: Mean Texture", fontsize=11, fontweight='semibold')
plt.legend(loc="upper right", framealpha=0.9, facecolor='#1e293b', edgecolor='gray')
plt.grid(True, linestyle=':', alpha=0.4, color='gray')

# Dark Theme aesthetics for premium look
ax.set_facecolor('#0f172a')
plt.gcf().patch.set_facecolor('#030712')
ax.spines['bottom'].color = 'gray'
ax.spines['left'].color = 'gray'
ax.tick_params(colors='gray')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
plt.title(label=plt.gca().get_title(), color='white')
for text in plt.gca().get_legend().get_texts():
    text.set_color('white')

print("[INFO] Displaying Plot Window...")
plt.show()
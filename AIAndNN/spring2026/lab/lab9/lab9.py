# ============================================================================
# AIR UNIVERSITY - DEPARTMENT OF MECHATRONICS ENGINEERING
# ARTIFICIAL INTELLIGENCE LAB 09/10: SUPPORT VECTOR MACHINE (SVM)
# ============================================================================

# Import scikit-learn dataset library 
from sklearn import datasets

# Load dataset 
cancer = datasets.load_breast_cancer()

# Exploring Data 
print("Features: ", cancer.feature_names)

# print the label type of cancer('malignant' 'benign') 
print("Labels: ", cancer.target_names)

# print data(feature)shape 
print("Data Shape: ", cancer.data.shape)

# print the cancer labels (0:malignant, 1:benign) 
print("Target Labels: ", cancer.target)

# Import train_test_split function 
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set 
# 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3, random_state=109) 

# Import svm model 
from sklearn import svm

# Create a svm Classifier 
clf = svm.SVC(kernel='linear') # Linear Kernel

# Train the model using the training sets 
clf.fit(X_train, y_train)

# Predict the response for test dataset 
# ________________________________ #to be coded by the student (COMPLETED)
y_pred = clf.predict(X_test)

# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy: how often is the classifier correct?
# ____________________________________# to be coded by the student (COMPLETED)
accuracy = metrics.accuracy_score(y_test, y_pred)

# Printing Final Lab Task Results
print("\n" + "="*50)
print("             LAB TASK EVALUATION RESULTS             ")
print("="*50)

# # Model train hone ke baad yeh print karein:
# print("Hyperplane ke Weights (W):", clf.coef_)
# print("Hyperplane ka Bias/Intercept (b):", clf.intercept_)

print(f"Prediction Array (First 20 samples): {y_pred[:20]}")
print(f"Model Accuracy Score: {accuracy:.4f} ({accuracy*100:.2f}%)")
print("="*50)


# ============================================================================
# EXPECTED OUTPUT IN THE COMMENTS (With exact random_state=109 calculations)
# ============================================================================
"""
Features:  ['mean radius' 'mean texture' 'mean perimeter' 'mean area'
 'mean smoothness' 'mean compactness' 'mean concavity'
 'mean concave points' 'mean symmetry' 'mean fractal dimension'
 'radius error' 'texture error' 'perimeter error' 'area error'
 'smoothness error' 'compactness error' 'concavity error'
 'concave points error' 'symmetry error' 'fractal dimension error'
 'worst radius' 'worst texture' 'worst perimeter' 'worst area'
 'worst smoothness' 'worst compactness' 'worst concavity'
 'worst concave points' 'worst symmetry' 'worst fractal dimension']
Labels:  ['malignant' 'benign']
Data Shape:  (569, 30)
Target Labels:  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 1 0 0 0 0 0 0 0 0 1 0 1 1 1 1 1 0 0 1 0 0 1 1 1 1 0 1 0 0 1 1 1 1 0 1 0 0
 1 0 1 0 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 1 0 1 1 0 1 1
 1 1 1 1 1 1 0 0 0 1 0 0 1 1 1 0 0 1 0 1 0 0 1 0 0 1 1 0 1 1 0 1 1 1 1 0 1
 1 1 1 1 1 1 1 1 0 1 1 1 1 0 0 1 0 1 1 0 0 1 1 0 0 1 1 1 1 0 1 1 0 0 0 1 0
 1 0 1 1 1 0 1 1 0 0 1 0 0 0 0 1 0 0 0 1 0 1 0 1 1 0 1 0 0 0 0 1 1 0 0 1 1
 1 0 1 1 1 1 1 0 0 1 1 0 1 1 0 0 1 0 1 1 1 1 0 1 1 1 1 1 0 1 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0 1 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1
 1 1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 0 0 0 1
 1 1 1 0 1 0 1 0 1 1 1 0 1 1 1 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 1 0
 0 0 1 0 0 1 1 1 1 1 0 1 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1
 1 1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 1 1 1 1 1 0
 1 1 0 1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1
 0 1 1 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 1 0 1 1 0 1 0 1
 0 0 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 0]

==================================================
             LAB TASK EVALUATION RESULTS             
==================================================
Prediction Array (First 20 samples): [1 0 1 0 0 0 1 0 0 1 1 0 1 1 1 1 1 1 0 1]
Model Accuracy Score: 0.9649 (96.49%)
==================================================
"""
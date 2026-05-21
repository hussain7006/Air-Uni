# Air University | Department of Mechatronics Engineering
## Artificial Intelligence Lab 09/10: Support Vector Machine (SVM)
### Complete Lecture & Explanation Script for Students (VS Code Edition)

> 💡 **Tip for Teacher:** Is file ko VS Code mein open karke `Ctrl + Shift + V` (Mac par `Cmd + Shift + V`) dabayein taake formatting, equations aur headings ka premium display show ho.

---

## 📌 Section 1: Introduction (Asal Kahani Kya Hai?)

Salam bacho! Aaj hum AI ki ek bohot hi powerful algorithm seekhne ja rahe hain jiska naam hai **Support Vector Machine (SVM)**. 

Pehle iska aam zindgi se concept samjhein. Farz karein aapki class mein do dushman qabile ya dushman groups hain (ek **Class A** aur ek **Class B**). Aapko in dono ke beech mein ek **Border Wall (Boundary)** banani hai taake inki aapas mein larai na ho. 

Aap wall kahan banayenge? Bilkul center mein, taake dono groups se wall ka faasla barabar aur sabse zyada ho. **Bas yahi kaam SVM ka hai!**

### 3 Main Pillars of SVM (Jo Viva m pucha jata hai):
1. **Hyperplane (The Decision Wall):** Do alag classes ke beech mein jo ideal separating line banti hai, use Hyperplane kehte hain. (Agar 2 features hon to yeh line hoti hai, agar zyada hon to ek flat sheet/surface hoti hai).
2. **Support Vectors (The Border Guards):** Dono groups ke woh badmash points jo border ke bilkul paas khare hote hain. Poori hyperplane inhi points ke sahare khari hoti hai. Agar yeh points apni jagah se hil jayein, to boundary badal jayegi.
3. **Margin (The Safe Gap):** Boundary wall se lekar sabse paas wale border guard (Support Vector) ke beech ka jo khali area hai, use Margin kehte hain. SVM ka main maqsad is margin ko **Maximize (sabse bada)** karna hota hai taake ghalti ka chance na rahe.

---

## 📌 Section 2: Medical Dataset Background (Breast Cancer)

Is lab manual mein hum jo data use kar rahe hain, woh real-world **Breast Cancer Wisconsin Dataset** hai. 
* Humare paas total **569 patients** ka data hai.
* Har patient ke body se tumor (rasoli) ka sample lekar uski **30 alag-alag khusushiyat (features)** check ki gayi hain (jaise radius, texture, perimeter, wagera).
* Humara target yeh dhoondna hai ke tumor **Malignant** (Khatarnak/Cancerous) hai ya **Benign** (Normal/Safe) hai.

---

## 📌 Section 3: Step-by-Step Python Code with Line Explanations

Neeche diye gaye code ko ghaur se dekhein. Isme aapke lab manual ke saare blanks fill kar diye gaye hain:

```python
# ============================================================================
# AIR UNIVERSITY - SVM CORE LAB CODE
# ============================================================================

# STEP 1: Libraries aur Dataset ko Import karna
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# Dataset load karein
cancer = datasets.load_breast_cancer()

# Data ko explore karna (Check karna ke andar kya hai)
print("1. Features List:\n", cancer.feature_names[:5]) # Pehle 5 features dikhane ke liye
print("\n2. Target Categories (Labels):", cancer.target_names) # ['malignant' 'benign']
print("3. Dataset Ki Shape:", cancer.data.shape) # (569, 30) -> 569 patients, 30 features
print("4. Raw Target Values (0 aur 1):", cancer.target[:20]) # Pehle 20 patients ka status

# ----------------------------------------------------------------------------
# STEP 2: Train-Test Split (Data ko do hisso m takseem karna)
# ----------------------------------------------------------------------------
# Hum 70% data computer ko seekhne (Train) ke liye denge.
# Aur 30% data computer ka exam lene (Test) ke liye chhupa kar rakhenge.
# random_state=109 aapke manual ke mutabiq exact shuffling set karta hai.

X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, 
    cancer.target, 
    test_size=0.3, 
    random_state=109
)

print(f"\n[INFO] Training samples: {X_train.shape[0]} | Testing samples: {X_test.shape[0]}")

# ----------------------------------------------------------------------------
# STEP 3: Model Creation & Training (AI Engine Activating)
# ----------------------------------------------------------------------------
# Hum Linear Kernel wala SVM Classifier bana rahe hain (Jo straight hyperplane banata hai)
clf = svm.SVC(kernel='linear') 

# Model ko fit/train karein (Yahan computer boundary seekh raha hai)
print("[INFO] Model training chal rahi hai...")
clf.fit(X_train, y_train)

# ----------------------------------------------------------------------------
# STEP 4: Predictions (AI Doctor Ka Test) - [Student Lab Task 1]
# ----------------------------------------------------------------------------
# Ab hum hidden X_test data computer ko de rahe hain aur keh rahe hain prediction karo
y_pred = clf.predict(X_test)

# ----------------------------------------------------------------------------
# STEP 5: Accuracy Calculation - [Student Lab Task 2]
# ----------------------------------------------------------------------------
# Asal answers (y_test) aur AI ke answers (y_pred) ko compare karke accuracy nikalna
accuracy = metrics.accuracy_score(y_test, y_pred)

# Results ko display karwana
print("\n" + "="*50)
print("             LAB TASK EVALUATION RESULTS             ")
print("="*50)
print(f"Prediction Array (First 20 samples): {y_pred[:20]}")
print(f"Model Accuracy Score: {accuracy:.4f} ({accuracy*100:.2f}%)")
print("="*50)
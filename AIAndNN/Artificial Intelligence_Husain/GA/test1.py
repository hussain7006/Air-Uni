texts = [
    "I love this movie",        # Positive
    "This film was terrible",   # Negative
    "Absolutely fantastic",     # Positive
    "It was worst",             # Negative      
    "I hated it",               # Negative
    "It was okay",              # Neutral/Positive
]
labels = [1, 0, 1, 0, 0, 1]  # 1 = Positive, 0 = Negative


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X, labels)


test_text = ["worst, love, terrible, love"]
X_test = vectorizer.transform(test_text)
prediction = model.predict(X_test)

print("Positive" if prediction[0] == 1 else "Negative") 




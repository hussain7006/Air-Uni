texts = ["I love this movie", "I hate this movie"]
labels = [1, 0]  # 1 = Positive, 0 = Negative


from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts).toarray()


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(10, activation='relu', input_shape=(X.shape[1],)),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, labels, epochs=10)

model.predict(vectorizer.transform(["I enjoy this"]).toarray())


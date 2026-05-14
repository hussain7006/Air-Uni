# First Feature: Weather condition
weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
           'Rainy','Sunny','Overcast','Overcast','Rainy']

# overcast = 0, rainy = 1, sunny = 2

# Second Feature: Temperature
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

# hot = 0, mild = 1, cool = 2

# Label or target variable: Whether to play or not
play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

# play = 0 for No, 1 for Yes

# Importing preprocessing tool from sklearn
# Importing preprocessing module to encode string labels into numbers
from sklearn import preprocessing 

# Creating labelEncoder to convert string labels into numbers
le = preprocessing.LabelEncoder()

# Converting 'weather' string labels into numbers
weather_encoded = le.fit_transform(weather)
print("Weather Encoded:", weather_encoded)

# Converting 'temp' string labels into numbers
temp_encoded = le.fit_transform(temp)
print("Temperature Encoded:", temp_encoded)

# Converting 'play' target labels into numbers (0 for No, 1 for Yes)
label = le.fit_transform(play)
print("Play Label Encoded:", label)

# Combining weather and temp into a single list of tuples (features)
combineFeatures = list(zip(weather_encoded, temp_encoded))
print("Combined combineFeatures:", combineFeatures)

# Importing KNN Classifier from sklearn
from sklearn.neighbors import KNeighborsClassifier

# Defining the model with K=3 neighbors
model = KNeighborsClassifier(n_neighbors=3)

# Training the model using the encoded combineFeatures and labels
model.fit(combineFeatures, label)

# Making a prediction for a new scenario [0, 2]
# Note: 0 and 2 are encoded values for weather and temperature
predicted = model.predict([[0, 2]])
# 0 = Overcast, 2 = Mild


print("Predicted Value for [0, 2]:", predicted)
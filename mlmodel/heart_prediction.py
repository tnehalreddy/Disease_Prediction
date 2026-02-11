import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression


heart_data = pd.read_csv("Disease_Prediction\mlmodel\heart.csv")

heart_data.head()

heart_data.tail()

heart_data.shape

heart_data.info()

heart_data.isnull().sum()

heart_data.describe()

heart_data["target"].value_counts()
X = heart_data.drop(columns="target", axis=1)
Y = heart_data["target"]

print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

print(X.shape, X_train.shape, X_test.shape)

# classifier = DecisionTreeClassifier(random_state=42)
# classifier = svm.SVC(kernel="linear")
# classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier = LogisticRegression()

classifier.fit(X_train, Y_train)

X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print("Accuracy on Training data : ", training_data_accuracy)

# accuracy on test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print("Accuracy on Test data : ", test_data_accuracy)
input_data = (62, 0, 0, 140, 268, 0, 0, 160, 0, 3.6, 0, 2, 2)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = classifier.predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0:
    print("The Person does not have a Heart Disease")
else:
    print("The Person has Heart Disease")

import pickle

filename = "heart_disease_model.sav"
pickle.dump(classifier, open(filename, "wb"))

# loading the saved model
loaded_model = pickle.load(open("heart_disease_model.sav", "rb"))

for column in X.columns:
    print(column)

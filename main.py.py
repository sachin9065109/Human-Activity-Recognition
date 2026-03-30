import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load data
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# Combine data
both = pd.concat([train, test])

# Features & target
X = both.drop("Activity", axis=1)
y = both["Activity"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Model
model = KNeighborsClassifier()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
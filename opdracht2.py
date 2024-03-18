import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv('data.csv')
df

sns.countplot(x='diagnosis', data=df)

df.corr()

df.isna().sum()

# Verwijder onnodige kolommen
data = df.drop(['Unnamed: 32'], axis=1)

# Encodeer de 'diagnosis'-kolom (Malignant: 1, Benign: 0)
le = LabelEncoder()
data['diagnosis'] = le.fit_transform(data['diagnosis'])

# Selecteer alleen de 'radius_mean' kolom als functie
X = data[['radius_mean']]
y = data['diagnosis']

# Split de data in trainings- en testsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiseer en train het Naive Bayes-model
model = GaussianNB()
model.fit(X_train, y_train)

# Voorspel de labels voor de testset
y_pred = model.predict(X_test)

# Bereken de nauwkeurigheid van het model
accuracy = accuracy_score(y_test, y_pred)
print(f"Nauwkeurigheid met alleen 'radius_mean' kolom: {accuracy * 100:.2f}%")

# Verwijder onnodige kolommen
data = df.drop(['Unnamed: 32'], axis=1)

# Encodeer de 'diagnosis'-kolom (Malignant: 1, Benign: 0)
le = LabelEncoder()
data['diagnosis'] = le.fit_transform(data['diagnosis'])

# Definieer features (X) en target (y)
X = data.drop(['id', 'diagnosis'], axis=1)
y = data['diagnosis']

# Split de data in trainings- en testsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiseer en train het Random Forest-model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Voorspel de labels voor de testset
y_pred = rf_model.predict(X_test)

# Bereken de nauwkeurigheid van het model
accuracy = accuracy_score(y_test, y_pred)
print(f"Nauwkeurigheid met Random Forest: {accuracy * 100:.2f}%")

# Toon andere evaluatiemetrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Toon de confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
